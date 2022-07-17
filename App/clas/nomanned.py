import sqlite3
from clas.Spaceship import spaceship
from wtforms import StringField, SelectField, SubmitField

class nomanned(spaceship):  
    velocidad=StringField("velocidad de vuelo")
    celdas= SelectField("Celdas fotovoltaicas", choices=[("Si"), ("No")])
    combustible= SelectField("Combustible", choices=[("tetróxido de nitrógeno"),("hidracina"), ("Mixto"), ("No usa")])            

    def crear(altura, peso, potencia, fuerza, velocidad, celdas, combustible, tipo):
        with sqlite3.connect("SPACESHIP.db") as con:
                cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL a ejecutar
                cursor.execute("INSERT INTO nomanned(Altura, Peso, Potencia, Fuerza, Velocidad, Fotovoltaicas, Combustible, Tipo, Estado) VALUES(?,?,?,?,?,?,?,?,?)", 
                [altura, peso, potencia, fuerza, velocidad, celdas, combustible, tipo, "Nueva"])
                con.commit()
                print("Funciona")

    def mejorar(self, id, altura, peso, potencia, fuerza, velocidad, celdas, combustible):
        with sqlite3.connect("SPACESHIP.db") as con:
                    cur = con.cursor()  # Manipular la BD
                    # Prepara la sentencia SQL a ejecutar
                    cur.execute("SELECT * FROM "+self+" WHERE id = ?", [id])
                    cur.execute('''UPDATE '''+self+''' SET Altura = ?, Peso = ?, Potencia = ?, Fuerza = ?, Velocidad = ?, Fotovoltaicas = ?, Combustible = ? WHERE id = ?''',
                     [altura, peso, potencia, fuerza, velocidad, celdas, combustible, id])
                    # Ejecuta la sentencia SQL
                    con.commit()
                    rows = cur.fetchall()  
                    return (rows)