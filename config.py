"""

    basic configuration

"""

from flask import Flask, render_template, url_for, redirect, request, session
# LoginManager

from flask_sqlalchemy import *
import os
import platform
import sys

# handling data and time var's
import datetime

# error handling
import traceback
import logging
logging.basicConfig(filename='server_messages.log', 
                    encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)
#logging.captureWarnings(False)

# My Own Funct
from MyFunc import *

app = Flask(__name__)
app.secret_key = 'HI TARZAN'

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'foods.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

basedir = os.path.abspath(os.path.dirname(__file__))
print(f"{FR_GREEN}............ basedir ===> {os.path.abspath(os.path.dirname(__file__))}{NO_COLOR}")

opSys = platform.system()
print(f"{FR_YELL}............ OS ===> {opSys}{NO_COLOR}")

#app.config['UPLOAD_FOLDER'] = 'img' 

from article_data import Articles
from excercise_data import Excercises
from LifeGame_data import LG_scripts
from EnigmaGame_data import Enigma_scripts

Articles = Articles()
Excercises = Excercises()
LG_scripts = LG_scripts()
Enigma_scripts = Enigma_scripts()

class Plato(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    tipo       = db.Column(db.String(10), nullable=False)
    nombre     = db.Column(db.String(30), nullable=False)
    precio     = db.Column(db.Float, nullable=False)
    disp       = db.Column(db.Integer, nullable=False, default=1)    
