from importlib.abc import Traversable
from operator import truediv
from tkinter.tix import Tree
from flask import Flask, render_template, request, flash, session, redirect
from clas.Spaceship import spaceship
from clas.shuttle import shuttle
from clas.manned import manned
from clas.nomanned import nomanned
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/home")
@app.route("/index")
@app.route("/", methods=["GET", "POST"])
def home():
     return render_template("home.html")

@app.route("/busqueda", methods=["GET", "POST"])
def search():    
    return render_template("search.html")

@app.route("/busqueda-all", methods=["GET", "POST"])
def searchall():
    rows1=manned.busq("manned")
    rows2=nomanned.busq("nomanned")
    rows3=shuttle.busq("shuttle")
    
    return render_template("search-all.html", trip=rows1, notrip=rows2, lanz=rows3)

@app.route("/busqueda-specific", methods=["GET", "POST"])
def searchspec():
    frm = spaceship()   
    v1=v2=v3=False
    t1=t2=t3=t4="None" 
    id=0
    pb=noman=shu=man=False    
    rows=manned.busq("manned")
    if 'search' in request.form:
        pb=False
        modelo = frm.modelo.data
        tipo=frm.tipo.data
        id=frm.id.data              
        modelo,v1,v2,v3=spaceship.model(modelo)
        rows=spaceship.busqe(modelo, id)    
        t1,t2,t3,t4=spaceship.type(tipo)
    if 'repair' in request.form: 
        pb=False
        modelo = frm.modelo.data
        id=frm.id.data              
        modelo,v1,v2,v3=spaceship.model(modelo)
        rows=spaceship.reparar(modelo, id)                   
    if 'improve' in request.form:  
        pb=False 
        modelo = frm.modelo.data     
        modelo,v1,v2,v3=spaceship.model(modelo)
        if v1==True:
            frm = manned() 
            man=True
        if v2==True:
            frm = noman() 
            noman=True
        if v3==True:
            frm = shuttle() 
            shu=True
    if 'update' in request.form:
       pb=True
    if 'act' in request.form:        
        modelo = frm.modelo.data
        act = frm.estado.data
        id=frm.id.data              
        modelo,v1,v2,v3=spaceship.model(modelo)
        rows=spaceship.actualizar(modelo, id, act)
        pb=False
    if 'send' in request.form:   
        id=frm.id.data      
        modelo = frm.modelo.data     
        modelo,v1,v2,v3=spaceship.model(modelo)
        if v1==True:
            frm = manned() 
            altura = frm.altura.data
            peso=frm.peso.data
            potencia=frm.potencia.data
            fuerza=frm.fuerza.data
            orbita=frm.orbita.data
            cap=frm.cap.data
            combustible=frm.combustible.data
            rows=manned.mejorar(modelo,id,altura, peso, potencia, fuerza, orbita, cap, combustible)
            man=False
        if v2==True:
            frm = noman() 
            altura = frm.altura.data
            peso=frm.peso.data
            potencia=frm.potencia.data
            fuerza=frm.fuerza.data
            velocidad=frm.velocidad.data
            celdas=frm.celdas.data
            combustible=frm.combustible.data
            rows=nomanned.mejorar(modelo, id, altura, peso, potencia, fuerza, velocidad, celdas, combustible)
            noman=False
        if v3==True:
            frm = shuttle() 
            altura = frm.altura.data
            peso=frm.peso.data
            potencia=frm.potencia.data
            fuerza=frm.fuerza.data
            cap=frm.cap.data
            combustible=frm.combustible.data
            rows=shuttle.mejorar(modelo, id, altura, peso, potencia, fuerza, cap, combustible)
            shu=False
    return render_template("search-specific.html", frm=frm,bd=rows, v1=v1, v2=v2, v3=v3, tipo1=t1, tipo2=t2, tipo3=t3, tipo4=t4, id=id, pb=pb,noman=noman,shu=shu,man=man)

@app.route("/busqueda-group", methods=["GET", "POST"])
def searchgrp():
    frm = spaceship()   
    rows1=manned.busq("manned")
    rows2=nomanned.busq("nomanned")
    rows3=shuttle.busq("shuttle")
    v1=v2=v3=False
    t1=t2=t3=t4="None"
    if request.method== 'POST':
        modelo = frm.Bmodelo.data
        tipo=frm.Btipo.data
        modelo,v1,v2,v3=spaceship.model(modelo)
        t1,t2,t3,t4=spaceship.type(tipo)             

    return render_template("search-group.html",frm=frm, trip=rows1, notrip=rows2, lanz=rows3, v1=v1, v2=v2, v3=v3, tipo1=t1, tipo2=t2, tipo3=t3, tipo4=t4)

@app.route("/crear", methods=["GET", "POST"])
def create():
    return render_template("create.html")

@app.route("/lanzadera", methods=["GET", "POST"])
def lanz():
    frm = shuttle()   
    if request.method== 'POST':
        altura = frm.altura.data
        peso=frm.peso.data
        potencia=frm.potencia.data
        fuerza=frm.fuerza.data
        cap=frm.cap.data
        combustible=frm.combustible.data
        tipo=frm.tipo.data        
        shuttle.crear(altura,peso,potencia,fuerza,cap,combustible,tipo)      
    return render_template("shuttle.html", frm=frm)

@app.route("/tripulada", methods=["GET", "POST"])
def trip():
    frm = manned()   
    if request.method== 'POST':
        altura = frm.altura.data
        peso=frm.peso.data
        potencia=frm.potencia.data
        fuerza=frm.fuerza.data
        orbita=frm.orbita.data
        cap=frm.cap.data
        combustible=frm.combustible.data
        tipo=frm.tipo.data
        manned.crear(altura,peso,potencia,fuerza,orbita,cap,combustible,tipo)
    return render_template("manned.html", frm=frm)

@app.route("/no-tripulada", methods=["GET", "POST"])
def notrip():
    frm = nomanned()   
    if request.method== 'POST':
        altura = frm.altura.data
        peso=frm.peso.data
        potencia=frm.potencia.data
        fuerza=frm.fuerza.data
        velocidad=frm.velocidad.data
        celdas=frm.celdas.data
        combustible=frm.combustible.data
        tipo=frm.tipo.data
        nomanned.crear(altura,peso,potencia,fuerza,velocidad,celdas,combustible,tipo)
    return render_template("no-manned.html", frm=frm)            

app.run(debug=True)
