import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class spaceship(FlaskForm):
    id= StringField("Id")
    altura = StringField("Altura")
    peso=StringField("Peso")
    potencia=StringField("potencia")
    estado=StringField("estado")
    fuerza=StringField("fuerza de empuje")
    tipo= SelectField("Tipo", choices=[("Búsqueda"),("Rescate"), ("Exploración"), ("Transporte")])
    modelo= SelectField("Modelo", choices=[("Tripulada"),("No tripulada"), ("Lanzadera")])
    
    Btipo= SelectField("Tipo", choices=[("Búsqueda"),("Rescate"), ("Exploración"), ("Transporte"), ("Todas")])
    Bmodelo= SelectField("Modelo", choices=[("Tripulada"),("No tripulada"), ("Lanzadera"), ("Todas")])    
    send=SubmitField("Crear")
    act=SubmitField("Actualizar")
    search=SubmitField("Buscar")
    repair = SubmitField("Reparar nave")
    improve = SubmitField("Actualizar caracteristicas de la nave")
    update = SubmitField("Actualizar estado de la nave")
    def busq(var):
        with sqlite3.connect("SPACESHIP.db") as con:
            # Convierte la respueta SQL a un diccionario
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM "+var)
            rows = cur.fetchall()    
            return (rows)
    
    def busqe(var, id):
        with sqlite3.connect("SPACESHIP.db") as con:
            # Convierte la respueta SQL a un diccionario
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM "+var+" WHERE id = ?", [id])
            rows = cur.fetchall()    
            return (rows)

    def reparar(self, id):
        with sqlite3.connect("SPACESHIP.db") as con:
                    cur = con.cursor()  # Manipular la BD
                    # Prepara la sentencia SQL a ejecutar
                    cur.execute("SELECT * FROM "+self+" WHERE id = ?", [id])
                    cur.execute('''UPDATE '''+self+''' SET Estado = ? WHERE id = ?''', ["Reparada",id])
                    # Ejecuta la sentencia SQL
                    rows = cur.fetchall()  
                    return (rows)

    def actualizar(self, id, act):
        with sqlite3.connect("SPACESHIP.db") as con:
                    cur = con.cursor()  # Manipular la BD
                    # Prepara la sentencia SQL a ejecutar
                    cur.execute("SELECT * FROM "+self+" WHERE id = ?", [id])
                    cur.execute('''UPDATE '''+self+''' SET Estado = ? WHERE id = ?''', [act,id])
                    # Ejecuta la sentencia SQL                    
                    rows = cur.fetchall()  
                    return (rows)

    def type(self):
        if(self=="Búsqueda"):
            t1="Búsqueda"
            t2=t3=t4="None"
        elif(self=="Rescate"):
            t2="Rescate"
            t1=t3=t4="None"
        elif(self=="Exploración"):
            t3="Exploración"
            t2=t1=t4="None"
        elif(self=="Transporte"):
            t4="Transporte"
            t2=t3=t1="None"
        else:
            t1="Búsqueda"
            t2="Rescate"
            t3="Exploración"
            t4="Transporte"
        return(t1,t2,t3,t4)

    def model(self):
        if(self=="Tripulada"):
            self="manned"
            v1=True
            v2=v3=False
        elif(self=="No tripulada"):
            self="nomanned"
            v2=True
            v1=v3=False
        elif(self=="Lanzadera"):
            self="shuttle"
            v3=True
            v2=v1=False
        else:
            v1=v2=v3=True
        return(self,v1,v2,v3)

    

