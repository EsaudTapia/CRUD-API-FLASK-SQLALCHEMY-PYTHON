from asyncio import Task
from msilib.schema import Class
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3307/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #para que no de warning 

db=SQLAlchemy(app) #sqlalchemy te paso la config de app
ma=Marshmallow(app)

