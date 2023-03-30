# 

from flask import Flask, render_template, url_for, redirect, request
# LoginManager

from article_data import Articles
from excercise_data import Excercises
from os import system

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = 'img' 

Articles = Articles()
Excercises = Excercises()

@app.route('/',methods=['GET', 'POST'])
def login():      
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            #return redirect(url_for('home'))
            return render_template('home.html')
        
    return render_template('login.html', error=error)


@app.route('/home')
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
    #
    #  code to update .bat file with excercise script
    #         

    return render_template('excercise.html', excercise = excercise)

@app.route('/pythonScript/')
def ExecPythonScript():

    # parameter from JS
    py_script_path = request.args['py_path']   
    #print("Excercise: " + file_path)

    """
    id = int(request.args['id'])    
    for i in range(len(Excercises)):
        if Excercises[i]['id'] == id:
            excercise = Excercises[i]
    py_file = excercise["fileDirPath"]            
    """
    from os import system

    # clear screen
    system('cls')    
       
    # execution string
    exec_command = 'cmd /c \"python.exe ' + py_script_path + '\"'
    system(exec_command)    
    
    return ""
    
    # to check later
        #system('cmd /c "z_execution_file.bat"')
        #system('cmd /c "python.exe static/py_excercises/20230227-OS-Examples/20230227-OS-Dir-Files-Example.py"')

    # relative path: 
        #file = open(r'openCmdLine.py','r').read()
        #file = open(r'z_execution_file.bat','r').read()    
        #file = open(r'z_execution_file-2.bat','r').read()
        #exec(file)    
    #return ""



@app.route('/project')
def project():
    return render_template('project.html')


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

if __name__ == '__main__':
    app.run(debug=True)