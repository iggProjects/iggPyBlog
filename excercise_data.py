from flask import url_for

def Excercises():
    

    excercises = [      
        {
            'id': 1, 
            'fileName': '20230213-PrototypeScript.py',            
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'Three functions in PrototypeScript.py',

            'homework': 'THESE functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables',

            'body': 'THESE functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables\nThese functions allows you to collect information about variables',          

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },
       
        {      
            'id': 2, 
            'fileName': '20230213-PrototypeScript.py',            
            'author': 'Igg',
            'date_created': '13-02-2023',
            'source_url': '',
            'section': 'my own functions and scripts',

            'homework': 'Make your base script',
            'body': 'Make your base script -- Make your base script -- Make your base script',

            'zip_url': '/static/py_excercises/20230213-Prototypescript/20230213-PrototypeScript.rar',  
            'img': '/img/icons8-consola-100.png'    
        },
 
        {
            'id': 10, 
            'fileName': 'OS Examples',            
            'author': 'Igg',
            'date_created': '26-01-2022',
            'source_url': 'https://docs.google.com/document/d/1XvFyC3xnEg6VGgrWOUcDmx1oNT6XALru59Kd0_SgGrk/edit#heading=h.xzp25aduswxa',
            'section': 'Python on the web',

            'homework': '-------------------------',
            'body': '------------------------',

            'zip_url': '/static/zip/20230227-OS-Dir-Files-Example_For_Teacher.zip',  
            'img': '/img/icons8-consola-100.png'          
            
        },
    ]

    return excercises