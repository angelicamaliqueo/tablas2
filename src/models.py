import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

db = sqlalchemy()

class User (db.Model):
    __tablename__ = "user"
    id = db.Column(ds.Integer,primary_Key=True)
    User_correo = db.Column(String(50))
    User_contraseña = db.Column(String(50))

class Capitulo (db.Model):
    __tablename__ = "capitulo"
    id = db.Column (db.Integer,primary_Key=True)
            capitulo_capitulo = db.Column(String(70))
            capitulo_nombre = db.Column((70)) 
            capitulo_informacion = db.Column(String(70))
            capitulo_detalle = db.Column(String(70))

class Personaje (db.Model):
    __tablename__ = "personaje"  
    id = db.Column (db.Integer,primary_Key=True)
    nombre = db.Column (String(70)) 
    imagen = db.Column (String(70))
    specie = db.Column (String(70))

classFvoritoCapitulo(db.Model):
    __tablename__ = "FavoritoCapitulo" 
    id = db.Column (db.Integer,primary_Key=True)
    Capitulo_id = db.Column(Integer, ForeignKey("capitulos.id"))
    user_id = db.Column(Integer, ForeignKey("user.id"))
    relacioncapitulo = relationship(Capitulo)
    relacionuser = relationship(User

class FavoritoPersonaje (db.Model):
    __tablename__ = "FavoritoPersonaje"
    id = db.Column (db.Integer,primary_Key=True) 
    FavoritoPersonaje_id = db.Column(Integer, ForeignKey(personaje.id))
    user_id = db.Column(Integer, ForeignKey("user.id")) 
    relacionpersonaje = relationship(Personaje) 
    relacionuser = relationship(User)  

def to_dict(self):
    return{}                   