# 

from flask import Flask, render_template, url_for, redirect, request
# LoginManager

from article_data import Articles
from excercise_data import Excercises
from LifeGame_data import LG_scripts
from EnigmaGame_data import Enigma_scripts

from flask_sqlalchemy import *
import os
#from os import system
#import subprocess

# COLOR CONTANTS
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"


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
    import subprocess
    # clear screen
    system('cls')
    print(f"{FR_YELL}======> Entrando en ExecPythonScript...{NO_COLOR}\n")
    
    # parameter from JS
    py_script_path = request.args['py_path']
    #print(f"===> File path:\n\t{py_script_path}")
    # execution string windows
    # exec_command = 'cmd /c \"python.exe ' + py_script_path + '\"'
    # system(exec_command) 
 
        
    # call subprocess to exceute py_script_path
    subprocess.run(["cmd", "/c", "python.exe", py_script_path])    
    # system('subprocess.run(["cmd", "/c", "python.exe", "01_LG-ExploracionMatrices_copy.py"])')

    # return ""

    #text = subprocess.run(["cmd", "/c", "dir .."],capture_output=True)
    #print(f"\n\n{FR_YELL}===> text type: {type(text)}{NO_COLOR}")
    #list_lines = text.stdout.splitlines()
    #print(f"\n\n{FR_YELL}===> text_lines type: {type(list_lines)}{NO_COLOR}")
    
    #for line in list_lines:
    #    print(f"{FR_GREEN}===> text_lines:{NO_COLOR} {line}")    

    print(f"{FR_YELL}======> saliendo ExecPythonScript...{NO_COLOR}\n")

    #result_script_exec(list_lines)
    #return redirect(url_for('about'))
    #return render_template('about')
    #return render_template('result_script_exec.html', text_lines = list_lines)
    #return redirect(url_for('result_script_exec'))
    
    #return render_template('result_script_exec.html')
    #return render_template('result_script_exec.html/?list_lines=' + str(list_lines))
    return ""

# https://stackoverflow.com/questions/37259740/passing-variables-from-flask-to-javascript
# https://www.youtube.com/watch?v=CJ3XiQgjNE8
# https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template


@app.route('/result_script_exec/')
def result_script_exec():
    print(f"{FR_YELL}\n======> Entrando en result...{NO_COLOR}\n")
    
    import subprocess, json
    from flask import Markup   

    # read path to script
    py_script_path = request.args['py_path']
    #print(f"py_path --> {py_script_path}")
    py_list = py_script_path.split('/')
    py_name = py_list[len(py_list)-1]
    #print(f"py_list: {py_list} --- {py_name}")

    # execute subprocess with script
    text = subprocess.run(["cmd", "/c", "python.exe", py_script_path],capture_output=True)    
    # text = subprocess.run(["cmd", "/c", "dir .."],capture_output=True)

    print(f"\n\n{FR_YELL}===> text type: {type(text)}{NO_COLOR}")
    list_b_lines = text.stdout.splitlines()
    list_color_text = []    
    #lines_colors = []
    for line in list_b_lines:
        #new_line = "<p>" + str(line) + "</p>"
        new_line = str(line)
        color = "black"
        if new_line == 'b\'\\x0c\\x1b[92m\'' or new_line == 'b\' \\x1b[00m\'' or new_line == 'b\'\\x1b[92m\'': 
            pass
        elif 'print empty line' in new_line:
            new_line = "---"
            color = "transparent"
            list = [color,new_line]
            list_color_text.append(list) 

            #print("=====> print empty line") 
        else: 
            print(f"0,1 --> {new_line[0:2]}")
            if "b'" in new_line[0:2]  or "b\"" in new_line[0:2]:
                print(f"0,1 ==> {new_line[0:2]}")
                new_line= new_line[2:]
            new_line = new_line.replace('-->','==>')
            new_line = new_line.replace('<','&lt;')
            #new_line = new_line.replace('<','<&nbsp;&nbsp;')
            new_line = new_line.replace('>','&gt;')
            #new_line = new_line.replace('>','&nbsp;>')
            new_line = new_line.replace('^','&nbsp;')
            new_line = new_line.replace(new_line[len(new_line)-1],'')
            #new_line = new_line.replace('\\n','')
            new_line = new_line.replace('\\n','<br>')
            new_line = new_line.replace('\\x1b[00m','')
            new_line = new_line.replace('\\t','&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')            
            
            if '\\x1b[91m' in new_line:
                new_line = new_line.replace('\\x1b[91m','')
                color = "red;"
            elif '\\x1b[92m' in new_line:
                new_line = new_line.replace('\\x1b[92m','')
                color= "green;" 
            elif '\\x1b[93m' in new_line:
                new_line = new_line.replace('\\x1b[93m','')
                color= "yellow;" 
            elif '\\x1b[94m' in new_line:
                new_line = new_line.replace('\\x1b[94m','')
                color= "blue;"
            elif '\\x1b[95m' in new_line:
                new_line = new_line.replace('\\x1b[95m','')
                color= "magenta;"
            else:
                pass

            print(f"line to print: {new_line}")
            new_line=Markup(new_line)
            list = [color,new_line]
            list_color_text.append(list) 
            
            print(f"new_line formatted => {list}")
    
    print(f"{FR_YELL}======> Saliendo de  result...{NO_COLOR}\n") 

    return render_template('result_script_exec.html',list_lines=list_color_text,py_name=py_name)


#
# MAIN
#

if __name__ == '__main__':
    app.run(debug=True)