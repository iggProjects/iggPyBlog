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
            
            'homework': 'Using multiple CPUs, execute in a few seconds the sum of the first 50,000 terms of each of the 10,000 arithmetic progressions. For that, use multiprocessing module. The central statement is: \"with multiprocessing.Pool(N_CPUS) as pool:\"',

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
            'title': 'Generate permutations of alphab of 26 chars',
            'fileDirPath': 'static/proj_enigmaGame_scripts/z-writePermut_26_File.py',  
            'fileDirPath1': 'static/proj_enigmaGame_scripts/z-writePermut_26_File_1.py',  
            
            'homework': 'For runtime reasons, in this exercise we will generate a file containing fifty thousand (50,000) permutations of \'abcdefghijklmnopqrstuvwxyz\' with a special condition: no letter in the permuted alphabet can match its position in the original alphabet.\n\nIt must be taken into account that if we want 5 million permutations, a file larger than 100 Mb will be generated, and we will have problems when synchronizing the update of the repository on Github. When generating files larger than 100 Mb, you must follow the guidelines for Git Large File Storage - https://git-lfs.github.com.\n\nHowever, for exercise number 3, we will use a file of 2 million permutations. If you want to do your own tests, download the py code (z-writePermut_26_File.py) using the "download button", and run the variants in number of permutations in a console on your pc, measuring execution time, number of permutations discarded, zize of the file, etc...',

            'body': 'The purpose of this code is to generate a text file containing millions of permutations of the 26-letter alphabet \'abcdefghijklmnopqrstuvwxyz\'. But permutations must meet a special condition: no letter in the permuted alphabet can match its position in the original alphabet. \n\nFor example, if we want 5 million permutations with the condition set, the processing time, using a single CPU on a machine with an Intel i7 processor, can be up to twenty minutes.\n\nThe algorithm is simple. Using the \'random.shuffle(orig_alphabet)\' command to generate a permutation, and then check if it satisfies the condition by verifying each letter in the generated list against the original alphabet list, in which case we proceed to save the alphabet as a string in the permutations file. A counter of alphabets that do not comply with the rule is kept and thus we know how many permutations fulfilled the rule and how many did not.\n\nFor exercise number 3, in which, using various CPUs of the machine, we will seek to decipher a short message prepared with one of the permutations included in the total of 2 million permutations.The interested person will be able to download the code via the \'download button\' on their own, and play with a larger number of permutations, as long as their computer has a good processor.\n\nIn this exercise, a multiprocess could have been conceived, in order to use all the CPUs of the machine and through a well-defined rule, ask each CPU to process the 2 million permutations. If the machine had 8 CPUs, 16 million alphabets would be obtained, and probably the execution time would not be much greater than what is realized here.\n\nTherefore, 16 million permuted alphabets is a very small number of the total number of alphabets that can be created. This leads us to a complex computational problem, in which thousands of computers would have to be combined with very clear distribution rules. In other words, deciphering a short message becomes a serious problem if any of the possible permutations is used, even if no letter matches its position in the original alphabet.',          

            'code_url': '/static/proj_enigmaGame_scripts/z-writePermut_26_File.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/z-writePermut_26-File.zip',  
            'img': '/img/icons8-consola-100.png'    
        },     

        {
            'id': 3,             
            'author': 'Igg',
            'date_created': '10-04-2023',
            'source_url': '',
            'section': 'Multiprocessing',
            'title': 'Use of two or more CPUs within your PC',
            'fileDirPath': 'static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-Alphab26.py',  
            'fileDirPath1': 'static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-Alphab26-1.py',  
            
            'homework': 'Encode a message with a "messy alphabet", and try to decode it reading millions permutations of the alphabet, each with the property that the permutated alphabet letter doesn\'t coincide with its position in the normal alphabet.',

            'body': 'With Multiprocessing we can use two or more CPUs units within a single computer system. It is the best approach to get the full potential from our hardware by utilizing full number of CPU cores available in our computer system.\n\n\'Manager class\' of multiprocessing module provides a way to coordinate shared information between all its users. A manager object controls a server process, which manages shared objects and allows other processes to manipulate them. In other words, managers provide a way to create data that can be shared between different processes. Following are the different properties of manager object. \n\nFor now, you can execute in console button, or download the .zip (download button) and execute .bat file in your local "downloads folder".\n\nTIP: create a folder called "py_files" inside "downloads", and move the .zip to that folder. Extract the files and run the .bat (with double click).\n\nNOTE: you must have python in the "path" of your pc, which you can check in "environment variables"',          

            'code_url': '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-Alphab26-vf.py',  
            'zip_url' : '/static/proj_enigmaGame_scripts/mpPoolManagerEnigmaRandom-vf.zip',  
            'img': '/img/icons8-consola-100.png'    
        },       
  
        

    ]

    return enigma_scripts