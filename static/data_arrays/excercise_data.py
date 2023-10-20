from flask import url_for

def Excercises():    

    excercises = [   

        {
            'id': 1,             
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Use colors to print',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors.py',
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors1.py',
            
            'homework': 'Printing with style is a good practice. Go ahead with some ideas to do it with colors.',
            
            'body': 'Ascii format for colors works very well with the print function. Constants can be used, or specific functions can be created to print messages with the desired effects.\n\nSOME CONSTANTS FOR FOREGROUND COLORS\n\tNO_COLOR="\\033[00m"\tFR_RED="\\033[91m"\tFR_GREEN="\\033\[92m"\tFR_YELL="\\033\[93m"\tFR_BLUE="\\033\[94m"\n\nSIMPLE SYNTAX FOR PRINTING "------- MAIN -------" WHEN STARTING THE PRINTING OF RESULTS\n\tprint(f"\\n{FR_GREEN}------- MAIN -------{NO_COLOR}\\n"):\n\nAN EXAMPLE OF FUNCTION TO PRINT SOME MESSAGE:\n\tdef prRed(msg):\n\t\tprint(f"{FR_YELL} {} {NO_COLOR}".format(msg))\n\tprRed("TESTING COLOR FUNCTION")\n\nLink: https://xdevs.com/guide/color_serial/',

            'code_url':'../static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-colors/20230213-PrototypeScript-colors.zip',  
            'img': '/img/icons8-consola-100.png'    
        },
       
 
         {      
            'id': 2, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Show Object Attributes',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-MostrarObject/0-prototype-mostrar-obj.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-MostrarObject/0-prototype-mostrar-obj1.py',            
            
            'homework': 'Use "mostrar(obj) function" to know properties and methods of some variables of interest used in your script.\nIn this case we use 2 variables: string and list. See script clicking in \"code button\".',

            'body': '# Show attributes and methods avalaible for "obj"\ndef mostrar(obj):\n\tif \'list\' in str(type(obj)) or \'tuple\' in str(type(obj)):\n\t\tprint(f"Object elements view in matrix form (8 columns by row)")\n\t\tmatrix_view(obj,8)\n\t# obj type and mem dir\n\tprint(f\"Object type is {type(obj)} and mem dir is: {id(obj)}")\n\t# obj attributes\n\t# attributes = [attr for attr in dir(obj) if not attr.startswith(\'__\')]\n\tattr_meth = [attr for attr in dir(obj)]\n\t# print attributes and methods in matrix form\n\tprint(f"Object assigned attributes and methods are:")\n\tmatrix_view(attr_meth,8)\n\tprint()\n\tprBG(\"-----------------END MOSTRAR OBJECT TYPE AND ATTRIB-METHODS-----------------",17)\n\tprint()',

            'code_url':'../static/py_excercises/20230213-PrototypeScript-MostrarObject/0-prototype-mostrar-obj.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-MostrarObject/20230213-PrototypeScript-MostrarObject.zip',  
            'img': '/img/icons8-consola-100.png'    
        },

         {      
            'id': 3, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Print in matrix form',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-MatrixView/0-prototype-matrix-view.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-MatrixView/0-prototype-matrix-view1.py',            
            
            'homework': 'Use "matrix_view(obj_l_t,n_cols) function" to print the elements of a list o tuple in matrix form.\n',

            'body': '# print \'lists-tuples\' in matrix form\ndef matrix_view(obj_l_t,n_cols):\n\tif \'list\' in str(type(obj_l_t)) or \'tuple\' in str(type(obj_l_t)):\n\t\timport math\n\t\tmatrix_rows=math.ceil(len(obj_l_t)/n_cols)\n\t\tlines=[]\n\t\tline=[]\n\t\ti=0\n\t\tfor i in  range(matrix_rows):\n\t\t\tfor j in range(n_cols):\n\t\t\t\tif i*n_cols+j<len(obj_l_t):\n\t\t\t\tline.append(obj_l_t[i*n_cols+j])\n\t\t\t\tprint(f"line: {i+1} --> {line}")\n\t\t\tline=[]\n\telse:\n\t\tprint(frRED(f"\\nWarning FROM matrix_view(): Object \'{obj_l_t}\' in not  list neither tupla !\\n" ))',          

            'code_url':'../static/py_excercises/20230213-PrototypeScript-MatrixView/0-prototype-matrix-view.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-MatrixView/20230213-PrototypeScript-MatrixView.zip',  
            'img': '/img/icons8-consola-100.png'    
        },        
         
        {      
            'id': 4, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Print Module Methods',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-ModuleMethods/0-prototype-mod-methods.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-ModuleMethods/0-prototype-mod-methods1.py',            
            
            'homework': 'Use "library_methods(my_lib) function" to print the methods of a library.\n',

            'body': 'def library_methods(my_lib):\n    for method in dir(my_lib):\n        LIB_method = method\n        print(f"FR_GREEN}{str(my_lib)}.method ==> {NO_COLOR}{LIB_method}")\n    print()',          

            'code_url':'../static/py_excercises/20230213-PrototypeScript-ModuleMethods/0-prototype-mod-methods.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-ModuleMethods/20230213-PrototypeScript-ModuleMethods.zip',  
            'img': '/img/icons8-consola-100.png'    
        },        

        {      
            'id': 5, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Print Help',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-HelpObj/0-prototype-help.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-HelpObj/0-prototype-help1.py',            
            
            'homework': 'Use "help_obj_method(obj) function" to call help option for a specific object. The Python help() function invokes the interactive built-in help system. If the argument is a string, then the string is treated as the name of a module, function, class, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is displayed.\n',

            'body': 'def help_obj_method(obj):\n    print(help(type(obj)))',          

            'code_url':'../static/py_excercises/20230213-PrototypeScript-HelpObj/0-prototype-help.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-HelpObj/20230213-PrototypeScript-HelpObj.zip',  
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 6, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Print related classes',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-RelatedClasses/0-prototype-related-classes.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-RelatedClasses/0-prototype-related-classes1.py',
            
            'homework': 'Use "relatedClasses(clas) function" to know the relations of a class. Method Resolution Order(__mro__) it denotes the way a programming language resolves a method or attribute.  MRO defines the order in which the base classes are searched when executing a method.\n',

            'body': 'def relatedClasses(clas):\n\n\tprint(f"\\n----- analysis of {FR_BLUE}"classes related"{NO_COLOR} with class \"{FR_GREEN}{clas}{NO_COLOR}\" -----\\n")\n\n\tfor clas_rel in clas.__mro__:\n \t\tprint(f"{FR_GREEN}\\trelated clas --> {clas_rel}\\n")\n\n\tprint(f"{NO_COLOR}----- end analysis -----")',          

            'code_url':'../static/py_excercises/20230213-PrototypeScript-RelatedClasses/0-prototype-related-classes.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-RelatedClasses/20230213-PrototypeScript-RelatedClasses.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 7, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Print Exception Hierarchy',
            'fileDirPath': 'static/py_excercises/20230218-PrototypeScript-Exception_Hierarchy/0-prototype-ExceptionHierarchy.py',            
            'fileDirPath1': 'static/py_excercises/20230218-PrototypeScript-Exception_Hierarchy/0-prototype-ExceptionHierarchy1.py',            
            
            'homework': ' TO DO ',

            'body': ' TO DO ',          

            'code_url':'../static/py_excercises/20230218-PrototypeScript-Exception_Hierarchy/0-prototype-ExceptionHierarchy.py',
            'zip_url': '../static/py_excercises/20230218-PrototypeScript-Exception_Hierarchy/20230218-PrototypeScript-Exception_Hierarchy.zip',                                                
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 8, 
            'author': 'Igg',
            'date_created': '30-04-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Upload the zip file of some dir',
            'fileDirPath': 'static/py_excercises/20230215-PrototypeScript-ZipFunc/0-prototype-ZipExample.py',            
            'fileDirPath1': 'static/py_excercises/20230215-PrototypeScript-ZipFunc/0-prototype-ZipExample1.py',            
            
            'homework': '',

            'body': '',

            'code_url':'../static/py_excercises/20230215-PrototypeScript-ZipFunc/0-prototype-ZipExample.py',
            'zip_url': '../static/py_excercises/20230215-PrototypeScript-ZipFunc/20230215-PrototypeScript-ZipFunc.zip',  
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 9, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'require_input_prompt': 'n',
            'section': 'Prototype Script',
            'title': 'Example of Try Exception when error occurs in <0-prototype-colors1.py>',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors-error.py',            
            'fileDirPath1': 'static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors-error1.py',                       
            'homework': '',

            'body': '',          

            'code_url':'../static/py_excercises/20230213-PrototypeScript-colors/0-prototype-colors-error.py',
            'zip_url': '../static/py_excercises/20230213-PrototypeScript-colors/20230213-PrototypeScript-colors-error.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 10, 
            'author': 'Igg',
            'date_created': '15-02-2023',
            'require_input_prompt': 'n',
            'section': 'Random Methods',
            'title': 'An experiment !',
            'fileDirPath': 'static/py_excercises/20230215-random-func/20230215-random_choice_experiment.py',            
            'fileDirPath1': 'static/py_excercises/20230215-random-func/20230215-random-choice-experiment1.py',            
            
            'homework': 'A short experiment to check behavior of \"random built-in function\".\n',

            'body': 'Native functions for random tests must respect the law of large numbers. Suppose we have a 6-sided die (1-6), and we roll it 10,000 times. what should the results be for each face? Well, let\'s try the random function that outputs a natural number between 1 and 6.\n\nDefine three variables:\n\tmy_dice = {\'1\':0,\'2\':0,\'3\':0,\'4\':0,\'5\':0,\'6\':0},\n\tideal_dice with 1/6 probability,\n\tand face_list=list(range(1,7)) to simulate numbre 1,2,3,4,5,6.\n\nThen make a loop to simulate 20 series of dice rolls each of one with increasing iterations according the rule iterations = 6000 * 2 * i, where i is the particular series called from main loop.',          

            'code_url':'../static/py_excercises/20230215-random-func/20230215-random_choice_experiment.py',
            'zip_url': '../static/py_excercises/20230215-random-func/20230215-random-func.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 11, 
            'author': 'Igg',
            'date_created': '20-02-2023',
            'require_input_prompt': 'y',
            'section': 'Input example',
            'title': 'Controling data type in input process',
            'fileDirPath': 'static/py_excercises/20230220-input/20230220-InputTrabajadores.py',            
            'fileDirPath1': 'static/py_excercises/20230220-input/20230220-InputTrabajadores1.py',            
            
            'homework': 'A simple input process with \"try -- except\" rules to control data type is correct. For example, see \"input_worker_age()\" function...',

            'body': 'Create the function \"input_worker_data()\" which will be called from a while loop in main.  This function calls 2 functions: Y_N() and input_worker_age(). Also contains 3 global variables (global moreData, workers, worker):\n\n\tmoreData boolean type,\n\tworkers as a list\n\tworker as dict.\n\nFunction Y_N() is checking if the user like to follow inserting workers o no.\n\nInitially, from main, the \"true\" value is assigned to moreData.\n\nPrincipal loop is as simple as:\n\twhile moreData:\n\t\tinput_worker_data()\n\nThe function input_worker_data() checks if the answer is correct and call Y_N() to know if process will continue worling or not (moreData \"true\" or \"false\").\n\n\"try except\" in  input_worker_age() function\n\ndef input_worker_age():\n\tglobal moreData,workers,worker\n\t try:\n\t\tworker_age=int(input(frRED("Please indicate \"age\" (integer between 18-65): ")))\n\t\tif worker_age in range(18,65):\n\t\t\tprint(frRED(f"age entered -> {worker_age}"))worker["age"] = worker_age\n\t\t\tworkers.append(worker)\n\t\t\t# ask for continue (Y,N)\n\t\t\tY_N()\n\t\telse:\n\t\t\tfrRED("Please indicate \"age\" (integer between 18-65): ")\n\t\t\tinput_worker_age()\n\texcept ValueError:\n\t\tfrRED("Please indicate \"age\" (integer between 18-65): ")\n\t\tinput_worker_age()',          

            'code_url':'../static/py_excercises/20230220-input/20230220-InputTrabajadores.py',
            'zip_url': '../static/py_excercises/20230220-input/20230220-input.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 12, 
            'author': 'Igg',
            'date_created': '23-02-2023',
            'require_input_prompt': 'n',
            'section': 'Encrypt a msg',
            'title': 'Get random alphabet to encrypt msg',
            'fileDirPath': 'static/py_excercises/20230223-enigma-Random/20230223-enigma-Random.py',            
            'fileDirPath1': 'static/py_excercises/20230223-enigma-Random/20230223-enigma-Random1.py',            
            
            'homework': 'Random suffle method to get messy alphabet, encode a message and decode after with this  messy alphab.',

            'body': '\t# create list of alphabet\n\tstring.ascii_lowercase "abcdefghijklmnopqrstuvwxyz"\n\talphab = list(string.ascii_lowercase)\n\told_alphab = list(string.ascii_lowercase)\n\tprint(frGREEN(f"{FR_YELL}Alphabet list{NO_COLOR}\\n{old_alphab}\\n"))\n\t# random.shuffle() to create new_alphab\n\trandom.shuffle(old_alphab)\n\tnew_alphab=old_alphab\n\tprint(frGREEN(f"{FR_GREEN}Messy alphabet list to encrypt{NO_COLOR}{new_alphab}\\n"))\n\tpause()',          

            'code_url':'../static/py_excercises/20230223-enigma-Random/20230223-enigma-Random.py',
            'zip_url': '../static/py_excercises/20230223-enigma-Random/20230223-enigma-Random.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 13, 
            'author': 'Igg',
            'date_created': '23-02-2023',
            'require_input_prompt': 'n',
            'section': 'Encrypt a msg',
            'title': 'Rotate alphabet twice to encrypt msg',
            'fileDirPath': 'static/py_excercises/20230223-enigma-Rotation/20230223-RotateAlphab-twice.py',            
            'fileDirPath1': 'static/py_excercises/20230223-enigma-Rotation/20230223-RotateAlphab-twice1.py',            
            
            'homework': 'Rotate twice with alphab[position:]  + alphab[:position] to get messy alphabet',

            'body': '# ask for position to rotate list\nposit1 = int(input("Position to obtain first alphab list rotation? "))\nalphab_01 = alphab[posit1:] + alphab[:posit1]\n\n# Printing list after left rotate\nprint (f"\\n{FR_YELL}First  alphabet after left rotate by {posit1}{NO_COLOR}\\n{str(alphab_01)}" )\n',          

            'code_url':'../static/py_excercises/20230223-enigma-Rotation/20230223-RotateAlphab-twice.py',
            'zip_url': '../static/py_excercises/20230223-enigma-Rotation/20230223-RotateAlphab-twice.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 14, 
            'author': 'Igg',
            'date_created': '27-02-2023',
            'require_input_prompt': 'n',
            'section': 'OS module',
            'title': 'OS methods',
            'fileDirPath': 'static/py_excercises/20230227-OS-Examples/20230227-OS-Dir-Files-Example.py',            
            'fileDirPath1': 'static/py_excercises/20230227-OS-Examples/20230227-OS-Dir-Files-Example1.py',            
            
            'homework': 'Working with paths, folders, files, .....',

            'body': '====== NEXT WEEK ======',          

            'code_url':'../static/py_excercises/20230227-OS-Examples/20230227-OS-Dir-Files-Example.py',
            'zip_url': '../static/py_excercises/20230227-OS-Examples/20230227-OS-Examples.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 15, 
            'author': 'Igg',
            'date_created': '27-02-2023',
            'require_input_prompt': 'n',
            'section': 'OS module',
            'title': 'Import function in a script that is in a parallel folder.',
            'fileDirPath': 'static/py_excercises/20230227-OS-Examples-2/py_script/20230227-ImportModuleFromParallel_folder.py',            
            'fileDirPath1': 'static/py_excercises/20230227-OS-Examples-2/py_script/20230227-ImportModuleFromParallel_folder1.py',            
            
            'homework': 'Import function in a script that is in a parallel folder.',

            'body': '====== NEXT WEEK ======',          

            'code_url':'../static/py_excercises/20230227-OS-Examples-2/py_script/20230227-ImportModuleFromParallel_folder.py',
            'zip_url': '../static/py_excercises/20230227-OS-Examples-2/20230227-OS-Examples-2.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 16, 
            'author': 'Igg',
            'date_created': '01-03-2023',
            'require_input_prompt': 'n',
            'section': 'OS module',
            'title': 'Delete repeated lines in file and sort',
            'fileDirPath': 'static/py_excercises/20230301-DelRepeatedLinesAndSort/20230301-DelRepeatedLinesAndSort.py',            
            'fileDirPath1': 'static/py_excercises/20230301-DelRepeatedLinesAndSort/20230301-DelRepeatedLinesAndSort1.py',            
            
            'homework': 'Use <SET> command to read a file and after delete repeated lines and <SORTED> command to sort the set to write in new file.',

            'body': 'Sequence of basic steps:\n\n\t1.- The central command is uniqlines = set(open(\'z-fileRepeatedLines.txt\').readlines()).\n\t2.- Then sort the set with uniqlines = sorted(uniqlines),\n\t3.- conclude with open(\'z-fileWithOutRepetitionLines.txt\', \'w\').writelines(uniqlines)\n\nSets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.\nA set is a collection which is unordered, unchangeable*, and unindexed.',          

            'code_url':'../static/py_excercises/20230301-DelRepeatedLinesAndSort/20230301-DelRepeatedLinesAndSort.py',
            'zip_url': '../static/py_excercises/20230301-DelRepeatedLinesAndSort/20230301-DelRepeatedLinesAndSort.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 17, 
            'author': 'Igg',
            'date_created': '01-03-2023',
            'require_input_prompt': 'n',
            'section': 'OS module',
            'title': 'Working with files',
            'fileDirPath': 'static/py_excercises/20230301-files_Read_write/20230301-WorkingWithFiles.py',            
            'fileDirPath1': 'static/py_excercises/20230301-files_Read_write/20230301-WorkingWithFiles1.py',            
            
            'homework': 'Read and write using OS methods',

            'body': '===== NEXT WEEK =====',          

            'code_url':'../static/py_excercises/20230301-files_Read_write/20230301-WorkingWithFiles.py',
            'zip_url': '../static/py_excercises/20230301-files_Read_write/20230301-WorkingWithFiles.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 18, 
            'author': 'Igg',
            'date_created': '08-03-2023',
            'require_input_prompt': 'n',
            'section': 'Working with Classes',
            'title': 'Nominas Class as example',
            'fileDirPath': 'static/py_excercises/20230308-classes-nominas/20230308-classes-Nominas.py',            
            'fileDirPath1': 'static/py_excercises/20230308-classes-nominas/20230308-classes-Nominas1.py',            
            
            'homework': 'This example work with \"related classes\" for \"Sistema Nómina\"',

            'body': 'Use "relatedClasses(Comercial)" function to see relations of "Comercial" object with other objects in Classes_Nomina.py. .\n\nUML schema\n\nEmpleado(id, nombre, año_ncto, dir_resid, cargo)\n\t\t⇧\n\t\t|\n\t\t|\n\t\textends\nSalarioEmpleado  (+ salario)     -----> sistemaNominas\n\t\t⇧\n\t\t| calculo_nomina():float\n\t\t|\n\t\textends\n\t\t|\nComercial (+ comision_ventas)\n\t\t|   calculo_nomina(): float',          

            'code_url':'../static/py_excercises/20230308-classes-nominas/20230308-classes-nominas.py',
            'zip_url': '../static/py_excercises/20230308-classes-nominas/20230308-classes-nominas.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 19, 
            'author': 'Igg',
            'date_created': '21-02-2023',
            'require_input_prompt': 'n',
            'section': 'String methods',
            'title': '',
            'fileDirPath': '',            
            'fileDirPath1': '',            
            
            'homework': '====== NEXT WEEK ======',

            'body': '',          

            'code_url':'../static/py_excercises/20230221-strings/20230221-strings.py',
            'zip_url': '',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 20, 
            'author': 'Igg',
            'date_created': '22-02-2023',
            'require_input_prompt': 'n',
            'section': 'String methods',
            'title': '',
            'fileDirPath': '',            
            'fileDirPath1': '',            
            
            'homework': '====== NEXT WEEK ======',

            'body': '',          

            'code_url':'../static/py_excercises/20230222-strings-Page33/20230222-page-33.py',
            'zip_url': '../static/py_excercises/20230222-strings-Page33/20230222-strings-Page33.zip',
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 21, 
            'author': 'Igg',
            'date_created': '27-02-2023',
            'require_input_prompt': 'n',
            'section': 'OS module',
            'title': 'Page 43-47',
            'fileDirPath': 'static/py_excercises/20230227-page-43to47/20230227_Page43to47.py',            
            'fileDirPath1': 'static/py_excercises/20230227-page-43to47/20230227_Page43to471.py',            
            
            'homework': '====== NEXT WEEK ======',

            'body': '',          

            'code_url':'../static/py_excercises/20230227-page-43to47/20230227_Page43to47.py',
            'zip_url': '../static/py_excercises/20230227-page-43to44/20230227_Page43to47.zip',
            'img': '/img/icons8-consola-100.png'    
        },



    ]

    return excercises
