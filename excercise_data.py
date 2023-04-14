from flask import url_for

def Excercises():    

    excercises = [   

        {
            'id': 0,             
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Why 0-prototype Script',
            'fileDirPath': '',           
            
            'homework': '',

            'body': '',
            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },

        {
            'id': 1,             
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Colors Function',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-colors/0-prototype.py',           
            
            'homework': 'Use colors for print. Printing with style is a good practice. Go ahead with some ideas.',

            'body': 'Ascii format for colors works very well with the print function. Constants can be used, or specific functions can be created to print messages with the desired effects.\n\nSOME CONSTANTS FOR FOREGROUND COLORS\n\tNO_COLOR="\\033[00m"\tFR_RED="\\033[91m"\tFR_GREEN="\\033\[92m"\tFR_YELL="\\033\[93m"\tFR_BLUE="\\033\[94m"\n\nSIMPLE SYNTAX FOR PRINTING "------- MAIN -------" WHEN STARTING THE PRINTING OF RESULTS\n\tprint(f"\\n{FR_GREEN}------- MAIN -------{NO_COLOR}\\n"):\n\nAN EXAMPLE OF FUNCTION TO PRINT SOME MESSAGE:\n\tdef prRed(msg):\n\t\tprint(f"{FR_YELL} {} {NO_COLOR}".format(msg))\n\tprRed("TESTING COLOR FUNCTION")',
            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },
       
        {      
            'id': 2, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Pause Function',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-PauseFunc/0-prototype.py',            
            
            'homework': 'Use "pause() function" to ask what to do after.',

            'body': '\n\ndef pause():\n    userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\\n")',

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },
 
         {      
            'id': 3, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Show Object Attributes',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-MostrarObject/0-prototype.py',            
            
            'homework': 'Use "mostrar(obj) function" to know properties and methods of certain varibles used in your script.',

            'body': '# Show attributes and methods avalaible for "obj"\ndef mostrar(obj):\n\tif type(obj) in [\'list\'\'dict\']:\n\t\tprint(f"Object elements view in matrix form (8 columns by row)")\n\t\tmatrix_view(obj,8)\n\t# obj type and mem dir\n\tprint(f\"Object type is {type(obj)} and mem dir is: {id(obj)}")\n\t# obj attributes\n\t# attributes = [attr for attr in dir(obj) if not attr.startswith(\'__\')]\n\tattr_meth = [attr for attr in dir(obj)]\n\t# print attributes and methods in matrix form\n\tprint(f"Object assigned attributes and methods are:")\n\tmatrix_view(attr_meth,8)\n\tprint()\n\tprBG(\"-----------------END MOSTRAR OBJECT TYPE AND ATTRIB-METHODS-----------------",17)\n\tprint()',

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },

         {      
            'id': 4, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Lists or Tuples in matrix form',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-MatrixView/0-prototype.py',            
            
            'homework': 'Use "matrix_view(obj_l_t,n_cols) function" to print the list o tuples elements in matrix form.\n',

            'body': '# print \'lists-tuples\' in matrix form\ndef matrix_view(obj_l_t,n_cols):\n\tif \'list\' in str(type(obj_l_t)) or \'tuple\' in str(type(obj_l_t)):\n\timport math\n\tmatrix_rows=math.ceil(len(obj_l_t)/n_cols)\n\tlines=[]\n\tline=[]\n\ti=0\n\tfor i in  range(matrix_rows):\n\tfor j in range(n_cols):\n\t\tif i*n_cols+j<len(obj_l_t):\n\t\tline.append(obj_l_t[i*n_cols+j])\n\t\tprint(f"line: {i+1} --> {line}")\n\t\tline=[]\n\telse:\n\t\tprint(frRED(f"\\nWarning FROM matrix_view(): Object \'{obj_l_t}\' in not  list neither tupla !\\n" ))',          

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },        
         
        {      
            'id': 5, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Module Methods',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-ModuleMethods/0-prototype.py',            
            
            'homework': 'Use "library_methods(my_lib) function" to print the methods of a library.\n',

            'body': 'def library_methods(my_lib):\n    for method in dir(my_lib):\n        LIB_method = method\n        print(f"FR_GREEN}{str(my_lib)}.method --> {NO_COLOR}{LIB_method}")\n    print()',          

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },        

        {      
            'id': 6, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Help',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-HelpObj/0-prototype.py',            
            
            'homework': 'Use "help_obj_method(obj) function" to call help option for a specific object.\n',

            'body': 'def help_obj_method(obj):\n    print(help(type(obj)))',          

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 7, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Know about related classes',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-RelatedClasses/0-prototype.py',            
            
            'homework': 'Use "relatedClasses(clas) function" to know the relations of a class.\n',

            'body': 'def relatedClasses(clas):\n    print(f"\\n----- analysis of {FR_BLUE}"classes related"{NO_COLOR} with class \"{FR_GREEN}{clas}{NO_COLOR}\" -----\\n")\n    for clas_rel in clas.__mro__:\n        print(f"{FR_GREEN}\\trelated clas --> {clas_rel}\\n")\n    print(f"{NO_COLOR}----- end analysis -----\\n")',          

            'zip_url': '--',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 8, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'MyFunc.py imported by 0-prototype.py',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-MyFunc/0-prototype.py',            
            
            'homework': 'List of my own functions in MyFunc.py imported by 0-prototype.py.\n',

            'body': 'Actual functions in MyFunc.py\n\tdef pause()\n\tdef Y_N(msg)\n\tdef Y_N_2(msg)\n\tdef matrix_view(obj_l_t,n_cols)\n\tdef library_methods(my_lib)\n\tdef mostrar(obj)\n\tdef ver_objetos(obj)\n\tdef ver_elementos(obj, todo=True)\n\tdef help_obj_method(obj)\n\tdef desc_obj_method(obj,todo=True)\n\tdef relatedClasses(clas)\n\tdef write_comments_log()',          

            'zip_url': '--',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 9, 
            'author': 'Igg',
            'date_created': '15-02-2023',
            'source_url': '',
            'section': 'Random Methods',
            'title': 'An experiment !',
            'fileDirPath': 'static/py_excercises/20230215-random-func/20230215-random_choice_experiment.py',            
            
            'homework': 'A short experiment to check behavior of random  built-in unction.\n',

            'body': 'Native functions for random tests must respect the law of large numbers. Suppose we have a 6-sided die (1-6), and we roll it 10,000 times. what should the results be for each face? Well, let\'s try the random function that outputs a natural number between 1 and 6.\n\nDefine three variables:\n\tmy_dice = {\'1\':0,\'2\':0,\'3\':0,\'4\':0,\'5\':0,\'6\':0},\n\tideal_dice with 1/6 probability,\n\tand face_list=list(range(1,7)) to simulate numbre 1,2,3,4,5,6.\n\nThen make a loop to simulate 20 series of dice rolls each of one with increasing iterations according the rule iterations = 10000 * 2 * i, where i is the particular series called from main loop.',          

            'zip_url': '--',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 10, 
            'author': 'Igg',
            'date_created': '15-02-2023',
            'source_url': '',
            'section': 'Input example',
            'title': 'Controling data type in input process',
            'fileDirPath': 'static/py_excercises/20230220-input/20230220-InputTrabajadores.py',            
            
            'homework': 'A simple input process with \"try\" \"except\" rules to control data type is correct.',

            'body': 'Create the function \"input_worker_data()\" which will be called from a while loop in main.  This function calls 2 functions: Y_N() and input_worker_age(). Also contains 3 global variables (global moreData, workers, worker):\n\n\tmoreData boolean type,\n\tworkers as a list\n\tand worker as dict.\n\nFunction Y_N() is checking if the user like to follow inserting workers o no.\n\nInitially, from main, the \"true\" value is assigned to moreData.\n\nPrincipal loop is as simple as:\n\twhile moreData:\n\t\tinput_worker_data()\n\nThe function input_worker_data() checks if the answer is correct and call Y_N() to know if process will continue worling or not (moreData \"true\" or \"false\").\n\n',          

            'zip_url': '--',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 11, 
            'author': 'Igg',
            'date_created': '15-02-2023',
            'source_url': '',
            'section': 'String methods',
            'title': '',
            'fileDirPath': 'static/py_excercises/20230222-strings-Page33/20230222-page-33.py',            
            
            'homework': '',

            'body': '',          

            'zip_url': '--',
            'img': '/img/icons8-consola-100.png'    
        },






        {
            'id': 20,             
            'author': 'Igg',
            'date_created': '26-01-2022',
            'source_url': 'https://docs.google.com/document/d/1XvFyC3xnEg6VGgrWOUcDmx1oNT6XALru59Kd0_SgGrk/edit#heading=h.xzp25aduswxa',
            'section': 'Python on the web',
            'title': '',
            'fileDirPath': 'OS Examples',            

            'homework': '-------------------------',

            'body': '------------------------',

            'zip_url': '--',  
            'img': '/img/icons8-consola-100.png'          
            
        },
    ]

    return excercises