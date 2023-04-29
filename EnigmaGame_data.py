from flask import url_for

def Enigma_scripts():    

    enigma_scripts = [      
        {
            'id': 1,             
            'author': 'Igg',
            'date_created': '27-03-2023',
            'source_url': '',
            'section': 'Multiprocessing',
            'title': 'Use of two or more CPUs within your PC',
            'fileDirPath': 'static/proj_enigmaGame_scripts/mpPool_Arith_Progres_Sum.py',  
            'fileDirPath1': 'static/proj_enigmaGame_scripts/mpPool_Arith_Progres_Sum1.py',  
            
            'homework': 'Execute in a few seconds the sum of the 50,000 terms\nof each of the 10,000 arithmetic progressions',

            'body': '................. Multiprocessing ....................\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).ºn\nNOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',          

            'code_url': '/static/proj_enigmaGame_scripts/mpPool_Arith_Progres_Sum.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/mpPool_Arith_Progres_Sum.zip',  
            'img': '/img/icons8-consola-100.png'    
        },     

        {
            'id': 2,             
            'author': 'Igg',
            'date_created': '27-03-2023',
            'source_url': '',
            'section': 'Multiprocessing',
            'title': 'Generate permutations of alphab of 15 chars',
            'fileDirPath': 'static/proj_enigmaGame_scripts/z-writePermut_15_File-v1.py',  
            'fileDirPath1': 'static/proj_enigmaGame_scripts/z-writePermut_15_File-v1-1.py',  
            
            'homework': 'Create the file \'z-permutFileSorted.txt\' whichs contains 500.000 permutationss\nof the substr \'a b c d e g i l m n o p r s u\' of alphab with size 15 chars.',

            'body': '................. Multiprocessing ....................\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).\n\nNOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',          

            'code_url': '/static/proj_enigmaGame_scripts/z-writePermut_15_File-v1.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/z-writePermut_15_File-v1.zip',  
            'img': '/img/icons8-consola-100.png'    
        },     

        {
            'id': 3,             
            'author': 'Igg',
            'date_created': '10-04-2023',
            'source_url': '',
            'section': 'Multiprocessing',
            'title': 'Use of two or more CPUs within your PC',
            'fileDirPath': 'static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.py',  
            'fileDirPath1': 'static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf-1.py',  
            
            'homework': 'Encode a message with a "messy alphabet", and try to decode it reading 500.000 permutations of the alphabet, each with the property that de permutated alphabet letter doesn\'t coincide with the it\'s position in the normal alphabet.',

            'body': '................. Multiprocessing ....................\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).\n\nNOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',          

            'code_url': '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       
  
        

    ]

    return enigma_scripts