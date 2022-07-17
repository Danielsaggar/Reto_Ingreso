import sqlite3
from clas.Spaceship import spaceship
from wtforms import StringField, SelectField, SubmitField

class shuttle(spaceship):
    cap=StringField("Capacidad de tripulantes")
    combustible= SelectField("Combustible", choices=[("químico sólido"),("propelente líquido"), ("oxígeno líquido"), ("petróleo refinado"), ("Mixto")])

    def crear(altura, peso, potencia, fuerza, cap, combustible, tipo):
        with sqlite3.connect("SPACESHIP.db") as con:
                cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL a ejecutar
                cursor.execute("INSERT INTO shuttle(Altura, Peso, Potencia, Fuerza, Capacidad, Combustible, Tipo, Estado) VALUES(?,?,?,?,?,?,?,?)", 
                [altura, peso, potencia, fuerza, cap, combustible, tipo, "Nueva"])
                # Ejecuta la sentencia SQL
                con.commit()
                print("Funciona")

    def mejorar(self, id, altura, peso, potencia, fuerza, cap, combustible):
        with sqlite3.connect("SPACESHIP.db") as con:
                    cur = con.cursor()  # Manipular la BD
                    # Prepara la sentencia SQL a ejecutar
                    cur.execute("SELECT * FROM "+self+" WHERE id = ?", [id])
                    cur.execute('''UPDATE '''+self+''' SET Altura = ?, Peso = ?, Potencia = ?, Fuerza = ?, Capacidad = ?, Combustible = ? WHERE id = ?''',
                     [altura, peso, potencia, fuerza, cap, combustible, id])
                    # Ejecuta la sentencia SQL
                    con.commit()
                    rows = cur.fetchall()  
                    return (rows)
    