# CONFIGURATION ENVIRONMENT AND VARIABLES

# APP and principal modules 
from config import *
# DB 
from config_DB import *
# DATA of excercises, articles, projects
from config_DATA import *

# app routes and functions

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

    try:         
        write_log_file("my_messages.txt","IN 'func excercises()'")
        return render_template('excercises.html', excercises = Excercises)

    except Exception as Argument:   
        """     
        logging.error(Argument)
        logging.warning(Argument)
        logging.info(Argument)
        logging.debug(Argument) 
        logging.critical(Argument)               
        """
        write_log_file("my_messages.txt","FROM 'func excercises(), SEE server_messages.log'")
        logging.exception("exception => "  + str(Argument))
        return render_template('error_page.html')

@app.route('/excercise/')
def display_excercise():
    excercise = 1
    id = int(request.args['id'])    
    for i in range(len(Excercises)):
        if Excercises[i]['id'] == id:
            excercise = Excercises[i]    
    return render_template('excercise.html', excercise = excercise)

@app.route('/excercise_input_example/')
def excercise_input_example():
    excercise = 1
    id = int(request.args['id'])    
    for i in range(len(Excercises)):
        if Excercises[i]['id'] == id:
            excercise = Excercises[i]    
    return render_template('excercise_input_example.html', excercise = excercise)


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

@app.route('/pythonScript/')
def ExecPythonScript():
    from os import system
    import subprocess

    # clear screen
    system('cls')
    print(f"{FR_YELL}======> Entrando en ExecPythonScript in console ...{NO_COLOR}\n")
    
    # parameter from JS
    py_script_path = request.args['py_path']
    print(f"{FR_GREEN} ===> File path:\n\t{py_script_path}{NO_COLOR}")
        
    # call subprocess to excecute py_script_path 
    if opSys == "Windows":        
        subprocess.run(["cmd", "/c", "python.exe", py_script_path])    
    elif opSys == "Linux":
        subprocess.run(["/usr/bin/bash", "-c", f"python {py_script_path}"])
    else:
        print(f"Please check how to pass list of parameters for operating system: {opSys}")
   
    #for line in list_lines:
    #    print(f"{FR_GREEN}===> text_lines:{NO_COLOR} {line}")    

    print(f"{FR_YELL}======> saliendo ExecPythonScript in console ...{NO_COLOR}\n")
   
    return ""

@app.route('/result_script_exec/')
def result_script_exec():
    print(f"{FR_YELL}\n====== in result_script_exec() for html ======{NO_COLOR}\n")
    from os import system
   
    import subprocess, json
    from flask import Markup   

    session['py_name'] = ""

    session['workers'] = ""

    session['list_lines'] = []
    session['list_JS_lines'] = []

    # read path to script
    py_script_path = request.args['py_path']
    print(f"py_path --> {py_script_path}")
    py_list = py_script_path.split('/')
    py_name = py_list[len(py_list)-1]
    print(f"py_list: {py_list}")
    print(f"script name: {py_name}")
    """
    # call subprocess to excecute py_script_path 
    if opSys == "Windows":        
        text = subprocess.run(["cmd", "/c", "python.exe", py_script_path],capture_output=True)    
    elif opSys == "Linux":
        text = subprocess.run(["/usr/bin/bash", "-c", f"python {py_script_path}"],capture_output=True)
    else:
        print(f"Please check how to pass list of parameters for operating system: {opSys}")
    """ 

    # call subprocess to excecute py_script_path
    if opSys == "Windows":
        text = subprocess.run(["cmd", "/c", "python.exe", py_script_path],capture_output=True)
    elif opSys == "Linux":
        # put mysite/ in path for "pythonanywhere"
        text = subprocess.run(["/usr/bin/bash", "-c", f"python {basedir}/{py_script_path}"],capture_output=True)
        #text = subprocess.run(["/usr/bin/bash", "-c", f"python mysite/{py_script_path}"],capture_output=True)
    else:
        print(f"Please check how to pass list of parameters for operating system: {opSys}")

    #print(f" ===> 'text'   type: {type(text)}")
    #print(f" ===> 'text' attrib: {dir(text)}")
    #print(f" ===> 'text'   data: {text}")    

    # see order in list_b_lines
    list_b_lines = text.stdout.splitlines()
    # print(f" ===> 'list_b_lines' type: {type(list_b_lines)}")
    # print(f" ===> 'list_b_lines' attrib: {dir(list_b_lines)}")
    # print(f" ===> 'list_b_lines' data: {list_b_lines}")

    for line in list_b_lines:
        print(f"==> line: {line}")

    list_color_text = []
    list_JS_lines = []
    #lines_colors = []

    for line in list_b_lines:
        #new_line = "<p>" + str(line) + "</p>"
        new_line = str(line)
        color = "black"
        if new_line == 'b\'\\x0c\\x1b[92m\'' or new_line == 'b\' \\x1b[00m\'' or new_line == 'b\'\\x1b[92m\'' or new_line == '\\x0c': 
            pass
        elif 'print empty line' in new_line:
            new_line = "---"
            color = "transparent"
            list = [color,new_line]
            list_color_text.append(list) 

            #print("=====> print empty line") 
        else: 
            #print(f"0,1 --> {new_line[0:2]}")
            if "b'" in new_line[0:2]  or "b\"" in new_line[0:2]:
                #print(f"0,1 ==> {new_line[0:2]}")
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
            
            if '\\x1b[91m' in new_line:      # red
                new_line = new_line.replace('\\x1b[91m','')
                color = "#800000"

            if '\\x1b[92m' in new_line:    # green
                new_line = new_line.replace('\\x1b[92m','')
                color= "green" 

            if '\\x1b[93m' in new_line:    # orange - (FR_YELL)
                new_line = new_line.replace('\\x1b[93m','')
                color= "#cc5200"    

            if '\\x1b[94m' in new_line:    # blue                
                new_line = new_line.replace('\\x1b[94m','')
                color= "blue"

            if '\\x1b[95m' in new_line:    # magenta
                new_line = new_line.replace('\\x1b[95m','')
                color= "magenta"

            """
            if '\\x1b[91m' in new_line:      # red
                new_line = new_line.replace('\\x1b[91m','')
                color = "#800000"                
            elif '\\x1b[92m' in new_line:    # green
                new_line = new_line.replace('\\x1b[92m','')
                color= "green" 
            elif '\\x1b[93m' in new_line:    # orange - (FR_YELL)
                new_line = new_line.replace('\\x1b[93m','')
                color= "#cc5200"            
            elif '\\x1b[94m' in new_line:    # blue                
                new_line = new_line.replace('\\x1b[94m','')
                color= "blue"
            elif '\\x1b[95m' in new_line:    # magenta
                new_line = new_line.replace('\\x1b[95m','')
                color= "magenta"
            else:
                pass
            """
            # Replace ',' by ';' in temp_line1[1] field for html printing effects
            new_line = new_line.replace(',',';')

            #print(f"line to print: {new_line}")
            js_line = new_line
            
            if '0' or '1' or '9' in js_line[0]:                
                list_JS_lines.append(js_line.replace(' ',''))
            else:
                pass

            new_line=Markup(new_line)
            list = [color,new_line]
            list_color_text.append(list) 
            
            print(f"new_line formatted => {list}")
    
    # print(f"list_JS_lines type: {type(list_JS_lines)} | first line: {list_JS_lines[2]}")
    
    # print(f"{FR_YELL}====== exit result_script_exec() in html ======{NO_COLOR}\n")
    
    # write list as text file
    # first case, output with matrix of (0,1,9) form from 'list_JS_lines' 
    # delete if exists    
    if os.path.exists("list_JS_lines.txt"):
        os.remove("list_JS_lines.txt")
        print(f"{FR_GREEN}........ old list_JS_lines.txt deleted")    
    
    with open(basedir + '/static/temp/list_JS_lines.txt', 'w') as f:
    #with open('list_JS_lines.txt', 'w') as f:
        for line in list_JS_lines:
            f.write(f"{line}\n")
    
    # second case, output with lines of text from 'list_color_text' 
    # delete if exists  
    if os.path.exists("list_text_lines.txt"):
        os.remove("list_text_lines.txt")
        print(f"{FR_GREEN}........ old list_text_lines.txt deleted")    

    # https://www.geeksforgeeks.org/python-save-list-to-csv/
    import csv

    # delete if exists  
    if os.path.exists("list_text_lines.csv"):
        os.remove("list_text_lines.csv")
        print(f"{FR_GREEN}........ old list_text_lines.csv deleted")    

    # data rows of csv file --> list_color_text
    with open(basedir + '/static/temp/list_text_lines.csv', 'w') as f:
    #with open('list_text_lines.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f,delimiter=",")
        write.writerows(list_color_text)

    """
    with open('list_text_lines.txt', 'w') as f:
        for line in list_color_text:
            f.write(f"{line}\n")
    """

    """
    with open('list_text_lines.txt', "w") as f:
        json.dump(list_color_text, f)
    """       
    
    # session variable to call render_template
    session['matrix_file_name'] = 'list_JS_lines.txt'
    session['textLines_file_name'] = 'list_text_lines.csv'

    session['py_name'] = py_name
    session['list_lines'] = list_color_text
    session['list_JS_lines'] = list_JS_lines    
    
    print(f"{FR_YELL}====== exit result_script_exec() in html ======{NO_COLOR}\n")
    print(f"{FR_YELL}====== go to result_script_exec.html ======{NO_COLOR}\n")

    # return redirect(url_for('result_script_html'))
    return render_template('result_script_exec.html',list_lines=list_color_text, list_JS_lines=list_JS_lines, py_name=py_name)


# subprocess with a dict as parameter
#   - https://stackoverflow.com/questions/48395685/launch-a-python-script-from-another-script-with-parameters-in-subprocess-argume
#   - https://www.askpython.com/python-modules/python-subprocess-module
#   - https://earthly.dev/blog/python-subprocess/


@app.route('/result_script_exec1/')
def result_script_exec1():
    print(f"{FR_YELL}\n====== in result_script_exec1() for html ======{NO_COLOR}\n")
    from os import system
   
    import subprocess, json
    from flask import Markup   

    #session['name'] = ""

    session['py_name'] = ""

    session['workers'] = ""
    
    session['list_lines'] = []
    session['list_JS_lines'] = []

    # read path to script
    py_script_path = request.args['py_path']
    print(f"py_path --> {py_script_path}")

    #workers = request.args.get("workers")
    workers = request.args['workers']    
    print(f"workers --> {workers}")
    workers_list = json.loads(workers)
    print(f"workers list var type: {type(workers_list)} | worker length: {len(workers_list)}")
    for k in workers_list:
        print(f"{k} -> {k[0]}, {k[1]} ")

    #for k in len(workers_list):
    #    print(f"key: {k}, value: {workers_list[k]}")
    
    py_list = py_script_path.split('/')
    py_name = py_list[len(py_list)-1]
    print(f"py_list: {py_list}")
    print(f"script name: {py_name}")
    
    # call subprocess to excecute py_script_path 
    #if opSys == "Windows":        
    #    text = subprocess.run(["cmd", "/c", "python.exe", py_script_path],capture_output=True)    
    #elif opSys == "Linux":
    #    text = subprocess.run(["/usr/bin/bash", "-c", f"python {py_script_path}"],capture_output=True)
    #else:
    #    print(f"Please check how to pass list of parameters for operating system: {opSys}")
     
    # call subprocess to excecute py_script_path
    if opSys == "Windows":
        text = subprocess.run(["cmd", "/c", "python.exe", py_script_path],capture_output=True)
    elif opSys == "Linux":
        # put mysite/ in path for "pythonanywhere"
        text = subprocess.run(["/usr/bin/bash", "-c", f"python mysite/{py_script_path}"],capture_output=True)
    else:
        print(f"Please check how to pass list of parameters for operating system: {opSys}")

    #print(f" ===> 'text'   type: {type(text)}")
    #print(f" ===> 'text' attrib: {dir(text)}")
    #print(f" ===> 'text'   data: {text}")    

    # see order in list_b_lines
    list_b_lines = text.stdout.splitlines()
    # print(f" ===> 'list_b_lines' type: {type(list_b_lines)}")
    # print(f" ===> 'list_b_lines' attrib: {dir(list_b_lines)}")
    # print(f" ===> 'list_b_lines' data: {list_b_lines}")

    for line in list_b_lines:
        print(f"==> line: {line}")

    list_color_text = []
    list_JS_lines = []
    #lines_colors = []

    for line in list_b_lines:
        #new_line = "<p>" + str(line) + "</p>"
        new_line = str(line)
        color = "black"
        if new_line == 'b\'\\x0c\\x1b[92m\'' or new_line == 'b\' \\x1b[00m\'' or new_line == 'b\'\\x1b[92m\'' or new_line == '\\x0c': 
            pass
        elif 'print empty line' in new_line:
            new_line = "---"
            color = "transparent"
            list = [color,new_line]
            list_color_text.append(list) 

            #print("=====> print empty line") 
        else: 
            #print(f"0,1 --> {new_line[0:2]}")
            if "b'" in new_line[0:2]  or "b\"" in new_line[0:2]:
                #print(f"0,1 ==> {new_line[0:2]}")
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
            
            if '\\x1b[91m' in new_line:      # red
                new_line = new_line.replace('\\x1b[91m','')
                color = "#800000"

            if '\\x1b[92m' in new_line:    # green
                new_line = new_line.replace('\\x1b[92m','')
                color= "green" 

            if '\\x1b[93m' in new_line:    # orange - (FR_YELL)
                new_line = new_line.replace('\\x1b[93m','')
                color= "#cc5200"    

            if '\\x1b[94m' in new_line:    # blue                
                new_line = new_line.replace('\\x1b[94m','')
                color= "blue"

            if '\\x1b[95m' in new_line:    # magenta
                new_line = new_line.replace('\\x1b[95m','')
                color= "magenta"


            # Replace ',' by ';' in temp_line1[1] field for html printing effects
            new_line = new_line.replace(',',';')

            #print(f"line to print: {new_line}")
            js_line = new_line
            
            if '0' or '1' or '9' in js_line[0]:                
                list_JS_lines.append(js_line.replace(' ',''))
            else:
                pass

            new_line=Markup(new_line)
            list = [color,new_line]
            list_color_text.append(list) 
            
            print(f"new_line formatted => {list}")
    
    # print(f"list_JS_lines type: {type(list_JS_lines)} | first line: {list_JS_lines[2]}")
    
    # print(f"{FR_YELL}====== exit result_script_exec() in html ======{NO_COLOR}\n")
    
    # write list as text file
    # first case, output with matrix of (0,1,9) form from 'list_JS_lines' 
    # delete if exists    
    if os.path.exists("list_JS_lines.txt"):
        os.remove("list_JS_lines.txt")
        print(f"{FR_GREEN}........ old list_JS_lines.txt deleted")    
    
    with open(basedir + '/static/temp/list_JS_lines.txt', 'w') as f:
        for line in list_JS_lines:
            f.write(f"{line}\n")
    
    # second case, output with lines of text from 'list_color_text' 
    # delete if exists  
    if os.path.exists("list_text_lines.txt"):
        os.remove("list_text_lines.txt")
        print(f"{FR_GREEN}........ old list_text_lines.txt deleted")    

    # https://www.geeksforgeeks.org/python-save-list-to-csv/
    import csv

    # delete if exists  
    if os.path.exists("list_text_lines.csv"):
        os.remove("list_text_lines.csv")
        print(f"{FR_GREEN}........ old list_text_lines.csv deleted")    

    # data rows of csv file --> list_color_text
    with open(basedir + '/static/temp/list_text_lines.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f,delimiter=",")
        write.writerows(list_color_text)

    
    #with open('list_text_lines.txt', 'w') as f:
    #    for line in list_color_text:
    #        f.write(f"{line}\n")
    

    #with open('list_text_lines.txt', "w") as f:
    #    json.dump(list_color_text, f)
           
    
    # session variable to call render_template
    session['matrix_file_name'] = 'list_JS_lines.txt'
    session['textLines_file_name'] = 'list_text_lines.csv'

    session['py_name'] = py_name
    session['list_lines'] = list_color_text
    session['list_JS_lines'] = list_JS_lines 

    session['workers'] = workers
    print(f"{FR_BLUE}worker name value --> {workers}")
    
    print(f"{FR_YELL}====== exit result_script_exec1() in html ======{NO_COLOR}\n")
    print(f"{FR_YELL}====== go to result_script_exec.html ======{NO_COLOR}\n")

    # return redirect(url_for('result_script_html'))
    return render_template('result_script_html.html',list_lines=list_color_text, list_JS_lines=list_JS_lines, py_name=py_name, workers=workers)
    #return render_template('result_script_exec.html',list_lines=list_color_text, list_JS_lines=list_JS_lines, py_name=py_name, name=name)


@app.route('/result_script_html')
def result_script_html():

    import json

    print("----------------------------------------------")
    py_name = session['py_name']
    print(f"py_name: {py_name}")

    workers = session['workers']

    print("----------------------------------------------")
    # read file of matrix lines
    matrix_file_name = basedir + "/static/temp/" + session['matrix_file_name'] 
    list_matrix_lines = []
    with open(matrix_file_name) as f:
        list_matrix_lines = f.readlines()        
    """
    for line in list_matrix_lines:
        print(f"{FR_GREEN}...... {line}")    
    """
    # read file of text lines
    textLines_file_name = basedir + "/static/temp/" + session['textLines_file_name'] 
    list_text_lines = []
    with open(textLines_file_name) as f:
        list_text_lines = f.readlines()
    
    print(f"{FR_GREEN}.....type of var list_text_lines: {type(list_text_lines)} | length: {len(list_text_lines)}{NO_COLOR}")    
    print(f"{FR_GREEN}.....type of var list_text_lines[0]: {type(list_text_lines[0])} | value: {list_text_lines[0]}{NO_COLOR}")
    print(f"{FR_GREEN}.....type of var list_text_lines[0]: {type(list_text_lines[0])} | value: {list_text_lines[0].split(',')}{NO_COLOR}")
    print(f"{FR_GREEN}.....type of var list_text_lines[0].split(','): {type((list_text_lines[0]).split(','))}")

    #print(f"{FR_GREEN}.....type of var list_text_lines[0][0]: {type(list_text_lines[0][0])} | value: {list_text_lines[0][0]}{NO_COLOR}")
    #print(f"{FR_GREEN}.....list: {list_text_lines}")   
    
    list_color_text_lines = []
    for line in list_text_lines:        
        temp_line1 = line.replace('\n','').split(',')
        #temp_line1 = temp_line1.split(',')       

        if len(temp_line1) > 1:
            #print(f"{FR_GREEN}list_text_lines---> {temp_line2}")    
            print(f"{FR_GREEN}list_text_lines---> {temp_line1[0]} | {temp_line1[1]}")
            list_color_text_lines.append(temp_line1)   
        
    print("----------------------------------------------")

    list_lines = session['list_lines']
    print(f"{FR_YELL}.....type of var list_lines: {type(list_lines)} | length: {len(list_lines)}{NO_COLOR}")
    print(f"{FR_YELL}.....type of var list_text_lines[0]: {type(list_lines[0])} | value: {list_lines[0]}{NO_COLOR}")    
    print(f"{FR_YELL}.....type of var list_text_lines[0][0]: {type(list_lines[0][0])} | value: {list_lines[0][0]}{NO_COLOR}") 
    #print(f"{FR_YELL}.....list: {list_lines}")   
    """
    for line in list_lines:
        print(f"{FR_YELL}list_lines===> {line}")    
    """
    print("----------------------------------------------")

    #list_JS_lines = session['list_JS_lines']
    #print(f"===== list_matrix_lines length:{NO_COLOR} {len(list_matrix_lines)}")
    #print("----------------------------------------------")
    #return render_template('result_script_html.html', list_lines=list_lines, list_JS_lines=list_matrix_lines, py_name=py_name)
    return render_template('result_script_html.html', list_lines=list_color_text_lines, list_JS_lines=list_matrix_lines, py_name=py_name, workers=workers)

#
# FOOD MENU EXAMPLE
#
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






#
# MAIN
#

if __name__ == '__main__':
    app.run(debug=True)
