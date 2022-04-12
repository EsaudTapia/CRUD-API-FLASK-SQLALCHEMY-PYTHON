from asyncio import tasks
from unittest import result
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3307/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #para que no de warning 

db=SQLAlchemy(app) #sqlalchemy te paso la config de app
ma=Marshmallow(app)

class Personaje(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(70), unique=True)
    descripcion = db.Column(db.String(255))
    serie =db.Column(db.String(100))
    
    def __init__(self,nombre,descripcion,serie) :
        self.nombre=nombre
        self.descripcion=descripcion
        self.serie=serie

db.create_all()

class personajeSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','descripcion','serie')
        
        
        
personaje_schema= personajeSchema()
personajes_schema= personajeSchema(many=True)


@app.route('/listapersonajes',methods=['GET'])
def listar_personaje():
    allPerso=Personaje.query.all()
    result= personajes_schema.dump(allPerso)
    return jsonify(result)


@app.route('/personajes',methods=['POST'])
def crear_personaje():
    
    nombreper= request.json['nombre']
    descripcion= request.json['descripcion']
    serie= request.json['serie']        
    nuevo_personaje=Personaje(nombreper,descripcion,serie)
    db.session.add(nuevo_personaje)
    db.session.commit()
    
    
    print(request.json)
    return personaje_schema.jsonify(nuevo_personaje)



if __name__ =='__main__':
    app.run(debug=True)















    
