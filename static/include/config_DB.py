"""

    basic configuration for DB

"""

from flask_sqlalchemy import *
import os, sys
from os.path import dirname, realpath

# import app
from config import app

# config DB 
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(dirname(__file__), 'foods.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# MENU EXAMPLE "plato" class
class Plato(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    tipo       = db.Column(db.String(10), nullable=False)
    nombre     = db.Column(db.String(30), nullable=False)
    precio     = db.Column(db.Float, nullable=False)
    disp       = db.Column(db.Integer, nullable=False, default=1)    
