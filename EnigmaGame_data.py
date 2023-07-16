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
            
            'homework': 'Using multiple CPUs, execute in a few seconds the sum of the first 50,000 terms of each of the 10,000 arithmetic progressions. For that, use multiprocessing module. The central statement is: \t\"with multiprocessing.Pool(N_CPUS) as pool:\"',

            'body': 'The first step is to determine how many cpus your laptop has. To do this, simply import the multiprocessing module.\nAlso, it is recommended to import the \'system\' module to clear the screen with \"system(\'cls\')\" command.\nUsing \'multiprocessing\', you can send each cpu the task of adding the first 10 thousand terms of the progression, and print the result. \nIn order not to fill the screen with all the results of the sums, it proceeds to print every 500 progressions.\nFor now, you can execute this example in the two console buttons (HTML, Console), or download the \'.zip\' (download button) and execute the ".bat file" in your local "downloads folder".\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).\nHINT: you must have python in the "path" of your pc, which you can check in "environment variables"\nNOTES:\n1.- Remember that when executing via the \'HTML\' button, you have to wait a bit until the execution of the code in the background ends, and pass the information to javascript to present it on the screen.\n2.- In the case of using the console button, being in "localhost", you must go to the console where you executed flask_app in VSC. ',          

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
            
            'homework': 'Encode a message with a "messy alphabet", and try to decode it reading 500.000 permutations of the alphabet, each with the property that the permutated alphabet letter doesn\'t coincide with its position in the normal alphabet.',

            'body': '................. Multiprocessing ....................\n\n============== DETAILS NEXT WEEK ==============\n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).\n\nNOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',          

            'code_url': '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       
  
        

    ]

    return enigma_scripts