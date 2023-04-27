def Articles():
    articles = [ 

        {
            'id': 0,          
            'title': 'Python Course experience.',   
            'author': 'Igg',
            'date_created': '20-04-2023',
            'section': 'The experience',           
            'summary': '',            
            'body': '',
            'page_url':'',
            'icon_img':'icons8-lectura-80.png'
        },

        {
            'id': 1, 
            'title': 'Connect PythonAnywhere with GitHub.',            
            'author': 'Kev in Tech',
            'date_created': '20-11-2022',
            'section':'',
            'summary': 'Connect your GitHub repository to PythonAnywhere! This make it much easier to develop your application locally then push your code to GitHub, and then deploy your app to PythonAnywhere!.',
            'body': '',
            'page_url': 'https://www.youtube.com/watch?v=4sTZN15J33A',
            'icon_img':'icons8-video-50.png'       
        },        

        {
            'id': 2, 
            'title': 'Google Colab: Python y Machine Learning en la nube.',            
            'author': 'Óscar Martín de la Fuente',
            'date_created': '4-06-2019',
            'section':'',
            'summary': 'En este tutorial veremos qué es y cómo utilizar Google Colab, la herramienta de Google en la nube para ejecutar código Python y crear modelos de Machine Learning a través de la nube de Google y con la posibilidad de hacer uso de sus GPU . Sí, has leído bien: con sus GPU y en la nube.',
            'body': '',
            'page_url': 'https://www.adictosaltrabajo.com/2019/06/04/google-colab-python-y-machine-learning-en-la-nube/',
            'icon_img':'icons8-lectura-80.png'
        },      

        {
            'id': 3, 
            'title': 'Google Colab: Python y Machine Learning en la nube.',            
            'author': 'Jake VanderPlas',
            'date_created': '16-08-2022',
            'section':'',
            'summary': 'Colab is a Jupyter Notebook-like product from Google Research. A Python program developer can use this notebook to write and execute random Python program codes just using a web browser. Also, you  can link your GitHub account with Google Colab to seamlessly import and export code files.',
            'body': '',
            'page_url': 'https://youtu.be/inN8seMm7UI',
            'icon_img':'icons8-video-50.png'       
        },      

        {
            'id': 4, 
            'title': 'Getting Started with Oracle LiveSQL.',            
            'author': ' holowczak',
            'date_created': '03-01-2017',
            'section':'',
            'summary': 'Oracle LiveSQL is a cloud based service that provides access to an Oracle 12c database instance. This database can be used to try many of the features of an Oracle 12c database without the need to install anything on a server or local PC. LiveSQL is especially useful for learning to program Oracle databases using Structured Query Language (SQL) and PL/SQL, Oracle’s procedural language extension to SQL.',
            'body': '',
            'page_url': 'https://holowczak.com/getting-started-with-oracle-livesql/',
            'icon_img':'icons8-lectura-80.png'       
        },


        {
            'id': 5, 
            'title': 'Stackoverflow Survey 2022.',            
            'author': 'survey.stackoverflow 2022',
            'date_created': '31-12-2022',
            'section':'',
            'summary': 'Visual Studio Code remains the preferred IDE across all developers. PyCharm is used more by people learning to code (26% vs 16%) while Vim is used more by Professional Developers (24% vs 16%).',
            'body': '',
            'page_url': 'https://survey.stackoverflow.co/2022/',
            'icon_img':'icons8-lectura-80.png'       
        },
        {
            'id': 6, 
            'title': 'Programming, scripting, and markup languages.',            
            'author': 'survey.stackoverflow 2022',
            'date_created': '31-12-2022',
            'section':'',
            'summary': 'Programming, scripting, and markup languages. 2022 marks JavaScript’s tenth year in a row as the most commonly used programming language. But, it’s a different picture for those learning to code. HTML/CSS, Javascript and Python are almost tied as the most popular languages for people learning to code. People learning to code are more likely than Professional Developers to report using Python (58% vs 44%), C++ (35% vs 20%), and C (32% vs 17%).',
            'body': '',
            'page_url': 'https://survey.stackoverflow.co/2022/#section-most-popular-technologies-programming-scripting-and-markup-languages',
            'icon_img':'icons8-lectura-80.png'                   
        },

        {
            'id': 7, 
            'title': 'Why is Python Growing So Quickly?',            
            'author': 'Devid Robinson',
            'date_created': '17-04-2017',
            'section':'',
            'summary': 'Why is Python Growing So Quickly? We recently showed that, based on Stack Overflow question visits, Python has a claim to being the fastest-growing major programming language, and that it has become the most visited tag on Stack Overflow within high-income countries.',
            'body': '',
            'page_url': 'https://stackoverflow.blog/2017/09/14/python-growing-quickly/',
            'icon_img':'icons8-lectura-80.png'                   
        },


        {
            'id': 8, 
            'title': 'Stack Overflow confirms Python’s popularity.',            
            'author': 'Richard Gall',
            'date_created': '10-04-2019',
            'section':'',
            'summary': 'Stack Overflow survey data further confirms Python’s popularity as it moves above Java in the most used programming language list. Three reasons for Python\'s growth: 1.- in Python’s easy to learn; 2.- The growth of data science and machine learning; 3.- Python is a flexible language.',
            'body': '',
            'page_url': 'https://hub.packtpub.com/stack-overflow-survey-data-further-confirms-pythons-popularity-as-it-moves-above-java-in-the-most-used-programming-language-list/',
            'icon_img':'icons8-lectura-80.png'                   
        },

        {
            'id': 9, 
            'title': 'Stack Overflow survey data further confirms Python’s popularity.',            
            'author': 'Matthew Harper',
            'date_created': '17-10-2022',
            'section':'',
            'summary': 'After its release in 1990 and experiencing a huge boom in popularity in the 2010s, Python has grown into one of the most widespread programming languages in the world. Many universities have begun teaching Python in their introduction to programming courses, and it’s a common first programming language for individuals learning how to code. Despite its popularity, Python is a controversial topic among software developers.',
            'body': '',
            'page_url': 'https://spin.atomicobject.com/2022/10/17/python-development/',
            'icon_img':'icons8-lectura-80.png'                   
        },

        {
            'id': 10, 
            'title': 'Top 8 Reasons for Using TypeScript / JavaScript (Node.js) instead of Python for z/OS.',            
            'author': 'Dan Kelosky',
            'date_created': '29-11-2022',
            'section':'',
            'summary': 'The TypeScript language came from Microsoft. The compiler is a “transpiler” that converts TypeScript to JavaScript. We’ll use data points for both TypeScript and JavaScript to make a case for their usage on z/OS. Here are 8 reasons why you might consider using TypeScript / JavaScript on z/OS instead of Python.',
            'body': '',
            'page_url': 'https://dkelosky.medium.com/top-8-reasons-for-using-typescript-javascript-node-js-instead-of-python-for-z-os-eb3e0b3f3cdc',
            'icon_img':'icons8-lectura-80.png'                   
        },

        {
            'id': 11, 
            'title': 'Why Python is not the programming language of the future',            
            'author': 'Ari Youry',
            'date_created': '31-05-2020',
            'section':'',
            'summary': 'Given the ubiquitous popularity of Python at the moment, it will surely take half a decade, maybe even a whole, for any of these new languages to replace it. Which of the languages it will be — Rust, Go, Julia, or a new language of the future — is hard to say at this point. But given the performance issues that are fundamental in the architecture of Python, one will inevitably take its spot.',
            'body': '',
            'page_url': 'https://towardsdatascience.com/why-python-is-not-the-programming-language-of-the-future-30ddc5339b66',
            'icon_img':'icons8-lectura-80.png'                   
        },

    ]

    return articles