"""

    basic configuration for DB

"""

from flask_sqlalchemy import *
import os
from config import app, basedir

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'foods.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

#app.config['UPLOAD_FOLDER'] = 'img' 

# MENU EXAMPLE "plato" class
class Plato(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    tipo       = db.Column(db.String(10), nullable=False)
    nombre     = db.Column(db.String(30), nullable=False)
    precio     = db.Column(db.Float, nullable=False)
    disp       = db.Column(db.Integer, nullable=False, default=1)    
