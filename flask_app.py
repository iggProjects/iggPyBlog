# 

from flask import Flask, render_template, url_for, redirect, request
# LoginManager

from article_data import Articles
from excercise_data import Excercises
from LifeGame_data import LG_scripts
from EnigmaGame_data import Enigma_scripts

from flask_sqlalchemy import *
import os
from os import system

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#print(f"............ basedir===> {basedir}")
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'foods.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Plato(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    tipo       = db.Column(db.String(10), nullable=False)
    nombre     = db.Column(db.String(30), nullable=False)
    precio     = db.Column(db.Float, nullable=False)
    disp       = db.Column(db.Integer, nullable=False, default=1)    

with app.app_context():
    db.create_all()


#app.config['UPLOAD_FOLDER'] = 'img' 

Articles = Articles()
Excercises = Excercises()
LG_scripts = LG_scripts()
Enigma_scripts = Enigma_scripts()

"""
@app.route('/',methods=['GET', 'POST'])
def login():      
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
            #return render_template('home.html')
        
    return render_template('login.html', error=error)
"""

@app.route('/')
#@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/course')
def course():
    return render_template('course.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/')
def display_article():
    article = 1
    id = int(request.args['id'])
    for i in range(len(Articles)):
        if Articles[i]['id'] == id:
            article = Articles[i]    
    return render_template('article.html', article = article)


@app.route('/excercises')
def excercises():
    return render_template('excercises.html', excercises = Excercises)

@app.route('/excercise/')
def display_excercise():
    excercise = 1
    id = int(request.args['id'])    
    for i in range(len(Excercises)):
        if Excercises[i]['id'] == id:
            excercise = Excercises[i]    
    return render_template('excercise.html', excercise = excercise)


@app.route('/food-menu')
def food_app():

    menu_del_dia = Plato.query.all()
    
    #menu_del_dia.sort(key=get_tipo)
    #print(f"menu del día: {menu_del_dia} | length: {len(menu_del_dia)}  | type: {type(menu_del_dia)}")
    #print(f"plato 1:  {menu_del_dia[1].nombre}") 
    entrada = []
    ppal   = []
    postre  = []
    errores = []

    for i in range(len(menu_del_dia)):
        if menu_del_dia[i].tipo == 'Entrada':
            entrada.append(menu_del_dia[i])
        elif menu_del_dia[i].tipo == 'Ppal':
            ppal.append(menu_del_dia[i])
        elif menu_del_dia[i].tipo == 'Postre':
            postre.append(menu_del_dia[i])
        else:
            errores.append(menu_del_dia[i])                                                                                                                                                                                                 
            print('upsssss somthing is wrong... 🙄')  

    #print(f"plato entrada:  {entrada[1].nombre}")  

    for i in range(len(entrada)):
        entrada[i].id = i +1

    for i in range(len(ppal)):
        ppal[i].id = i +1

    for i in range(len(postre)):
        postre[i].id = i +1

    return render_template('food-menu.html', entrada=entrada, ppal=ppal, postre=postre)

@app.route('/foods_login',methods=['GET', 'POST'])
def foods_login():      
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('foods_home_admin'))
            #return render_template('foods_home_admin.html')
        
    return render_template('foods_login.html', error=error)

@app.route('/foods_home_admin')
def foods_home_admin():
    return render_template('foods_home_admin.html')

@app.route('/foods_reg_matrix')
def foods_reg_matrix():    
    platos = Plato.query.all()
    return render_template('foods_reg_matrix.html', platos=platos)

@app.route('/foods_reg_insert',methods=['POST','GET'])
def foods_reg_insert():
    if request.method == 'POST':

        plato_nuevo = Plato()
        plato_nuevo.tipo = request.form['fTipo']
        plato_nuevo.nombre = request.form['fNombre']
        plato_nuevo.precio = request.form['fPrecio']
        plato_nuevo.disp = 1   

        print("plato_nuevo ----> " + plato_nuevo.nombre)
        #plato_nuevo.verified = True
        db.session.add(plato_nuevo)
        db.session.commit()

        return redirect(url_for("foods_reg_matrix"))    
    
    return render_template('foods_reg_insert.html')

@app.route('/foods_reg_update/<string:uid>', methods=['POST','GET'])
def foods_reg_update(uid):  
    if request.method == 'POST':

        plato_mod = Plato.query.get(uid)
        plato_mod.tipo = request.form['fTipo']
        plato_mod.nombre = request.form['fNombre']
        plato_mod.precio = request.form['fPrecio']
        plato_mod.disp = 1   

        db.session.commit()

        return redirect(url_for("foods_reg_matrix"))    

    
    plato = Plato.query.get(uid)
    return render_template('foods_reg_update.html', plato=plato)

@app.route('/foods_reg_delete/<string:uid>', methods=['GET'])
def foods_reg_delete(uid):  
    plato=Plato.query.get(uid)
    db.session.delete(plato)    
    db.session.commit()
    return redirect(url_for('foods_reg_matrix'))
    #return render_template('reg_matrix.html')



# ==================================================================================#

@app.route('/project-EnigmaGame')
def project_EnigmaGame():    
    return render_template('project-EnigmaGame.html', enigma_scripts = Enigma_scripts)

@app.route('/project-EnigmaGame_script/')
def display_EnigmaGame_script():
    enigma_script = 1
    id = int(request.args['id'])    
    for i in range(len(Enigma_scripts)):
        if Enigma_scripts[i]['id'] == id:
            enigma_script = Enigma_scripts[i]    
    return render_template('project-EnigmaGame_script.html', enigma_script = enigma_script)


@app.route('/project-LifeGame')
def project_LifeGame():
    return render_template('project-LifeGame.html', lg_scripts = LG_scripts)

@app.route('/project-LifeGame_script/')
def display_LifeGame_script():
    lg_script = 1
    id = int(request.args['id'])    
    for i in range(len(LG_scripts)):
        if LG_scripts[i]['id'] == id:
            lg_script = LG_scripts[i]    
    return render_template('project-LifeGame_script.html', lg_script = lg_script)


@app.route('/about')
def about():
    return render_template('about.html')

"""
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            #return redirect(url_for('home'))
            return render_template('home.html')
        
    return render_template('login.html', error=error)
"""

@app.route('/pythonScript/')
def ExecPythonScript():
    from os import system
    # parameter from JS
    py_script_path = request.args['py_path']
    #print(f"===> File path:\n\t{py_script_path}")
    # clear screen
    system('cls')
    # execution string
    exec_command = 'cmd /c \"python.exe ' + py_script_path + '\"'
    system(exec_command)    
    
    return ""    
#
# MAIN
#

if __name__ == '__main__':
    app.run(debug=True)