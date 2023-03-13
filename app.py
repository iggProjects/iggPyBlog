# 

from flask import Flask, render_template, url_for, request
from article_data import Articles
import os


app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = 'img' 

Articles = Articles()

@app.route('/')
def index():    
    return render_template('home.html')


@app.route('/course')
def course():
    return render_template('course.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


@app.route('/article/')
def display_article():
    article = 10
    id = int(request.args['id'])
    #print("len Articles",len(Articles))
    for i in range(len(Articles)):
        if Articles[i]['id'] == id:
            article = Articles[i]
    #print(id," -- ", article, " -- " , Articles[1])        
    return render_template('article.html', article = article)

@app.route('/excercises')
def excercises():
    return render_template('excercises.html')

@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run(debug=True)


