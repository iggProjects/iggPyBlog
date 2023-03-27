from flask import url_for

def Excercises():    

    excercises = [      
        {
            'id': 1,             
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Colors Function',
            'fileDirPath': 'static/py_excercises/20230213-PrototypeScript/0-prototype.py',            
            
            'homework': 'Use colors for print.\n',

            'body': 'Printing with style is a good practice.....',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },
       
        {      
            'id': 2, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Pause Function',
            'fileDirPath': '---',            
            
            'homework': 'Use "pause() function" to ask what to do after.\n',

            'body': 'def pause():\n    userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\\n")\n\nA\nB\nC\n ',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },
 
         {      
            'id': 3, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Show Object Attributes',
            'fileDirPath': '---',            
            
            'homework': 'Use "mostrar(obj) function" to know prpperties and methods of certain varibles used in script.\n',

            'body': '-----------------',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },

         {      
            'id': 4, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Lists or Tuples in matrix form',
            'fileDirPath': '---',            
            
            'homework': 'Use "matrix_view(obj_l_t,n_cols) function" to print the list o tuples elements in matrix form.\n',

            'body': '----------------',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },        
         
        {      
            'id': 5, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Module or Library Methods',
            'fileDirPath': '---',            
            
            'homework': 'Use "library_methods(my_lib) function" to print the methods of a library.\n',

            'body': 'def library_methods(my_lib):\n    for method in dir(my_lib):\n        LIB_method = method\n        print(f"FR_GREEN}{str(my_lib)}.method --> {NO_COLOR}´{LIB_method}")\n    print()',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },        

        {      
            'id': 6, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Print Help',
            'fileDirPath': '---',            
            
            'homework': 'Use "help_obj_method(obj) function" to call help option for a specific object.\n',

            'body': 'def help_obj_method(obj):\n    print(help(type(obj)))',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },

        {      
            'id': 7, 
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Prototype Script',
            'title': 'Know about related classes',
            'fileDirPath': '---',            
            
            'homework': 'Use "relatedClasses(clas) function" to know the relations of a class.\n',

            'body': 'def relatedClasses(clas):\n    print(f"\\n----- analysis of {FR_BLUE}"classes related"{NO_COLOR} with class \"{FR_GREEN}{clas}{NO_COLOR}\" -----\\n")\n    for clas_rel in clas.__mro__:\n        print(f"{FR_GREEN}\\trelated clas --> {clas_rel}\\n")\n    print(f"{NO_COLOR}----- end analysis -----\\n")',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
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

            'zip_url': '/static/zip/20230227-OS-Dir-Files-Example_For_Teacher.zip',  
            'img': '/img/icons8-consola-100.png'          
            
        },
    ]

    return excercises