from flask import url_for

def LG_scripts():    

    lg_scripts = [      
        {
            'id': 1,             
            'author': 'Igg',
            'date_created': '01-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Working with Matrices',
            'fileDirPath': 'static/proj_lifeGame_scripts/01_LG-ExploracionMatrices.py',
            'fileDirPath1': 'static/proj_lifeGame_scripts/01_LG-ExploracionMatrices1.py',
            
            'homework': 'Manipulate matrices with numpy',

            'body': 'To work with matrices Numpy is a very powerful module, rich in methods.\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/01_LG-ExploracionMatrices.py',  
            'zip_url': '/static/proj_lifeGame_scripts/01_LG-ExploracionMatrices.zip',  
            'img': '/img/icons8-consola-100.png'    
        },     

        {
            'id': 2,             
            'author': 'Igg',
            'date_created': '02-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Expand and contract matrices',
            'fileDirPath': 'static/proj_lifeGame_scripts/02_LG-expandir-contraer-funciones.py',            
            'fileDirPath1': 'static/proj_lifeGame_scripts/02_LG-expandir-contraer-funciones1.py',            
            
            'homework': 'First step in life game: create custom matrices to apply the \"game of life\" algorithm',

            'body': 'Expand and contract matrices with numpy !\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/02_LG-expandir-contraer-funciones.py',  
            'zip_url': '/static/proj_lifeGame_scripts/02_LG-expandir-contraer-funciones.zip',  
            'img': '/img/icons8-consola-100.png'    
        },     

        {
            'id': 3,             
            'author': 'Igg',
            'date_created': '03-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Expand and contract matrices',
            'fileDirPath': 'static/proj_lifeGame_scripts/03_LG-reglas.py',            
            'fileDirPath1': 'static/proj_lifeGame_scripts/03_LG-reglas1.py',            
            
            'homework': 'Simulate Game of Life iterations',

            'body': '\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/03_LG-reglas.py',  
            'zip_url': '/static/proj_lifeGame_scripts/03_LG-reglas.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       

        {
            'id': 4,             
            'author': 'Igg',
            'date_created': '04-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Expand and contract matrices',
            'fileDirPath': 'static/proj_lifeGame_scripts/04_LG-iterations-funciones.py',            
            'fileDirPath1': 'static/proj_lifeGame_scripts/04_LG-iterations-funciones1.py',            
            
            'homework': 'Functions to invoke in MAIN of Game of Life script',

            'body': '\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/04_LG-iterations-funciones.py',  
            'zip_url': '/static/proj_lifeGame_scripts/04_LG-iterations-funciones.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       

        {
            'id': 5,             
            'author': 'Igg',
            'date_created': '05-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Expand and contract matrices',
            'fileDirPath': 'static/proj_lifeGame_scripts/05_LG-Iterations-ejec-normal.py',            
            'fileDirPath1': 'static/proj_lifeGame_scripts/05_LG-Iterations-ejec-normal1.py',            
            
            'homework': 'Execute 500 iterations of Game of Life script',

            'body': '\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/05_LG-Iterations-ejec-normal.py',  
            'zip_url': '/static/proj_lifeGame_scripts/05_LG-Iterations-ejec-normal.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       

        {
            'id': 6,             
            'author': 'Igg',
            'date_created': '05-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Simulate set of 4 games (matrices)',
            'fileDirPath': 'static/proj_lifeGame_scripts/06_LG-show-four-matrices.py',            
            'fileDirPath1': 'static/proj_lifeGame_scripts/06_LG-show-four-matrices1.py',            
            
            'homework': 'Execute 500 iterations of Game of Life script.',

            'body': '\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/06_LG-show-four-matrices.py',  
            'zip_url': '/static/proj_lifeGame_scripts/06_LG-show-four-matrices.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       

        {
            'id': 7,             
            'author': 'Igg',
            'date_created': '05-04-2023',
            'source_url': '',
            'section': 'Game of life',
            'title': 'Simulate set of 4 games (matrices)',
            'fileDirPath': 'static/proj_lifeGame_scripts/07-LG_-multiprocessing-cpu.py',            
            'fileDirPath1': '',            
            
            'homework': 'Execute Sets of 4 Games with multiprocessing.',

            'body': '\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click). NOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',  

            'code_url': '/static/proj_lifeGame_scripts/07-LG_-multiprocessing-cpu.py',  
            'zip_url': '/static/proj_lifeGame_scripts/07-LG_-multiprocessing-cpu.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       

    ]

    return lg_scripts