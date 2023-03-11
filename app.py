# 

from flask import Flask
from flask import Flask, render_template
from article_data import Articles


app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    #return "<center>Kaixo Team !</center>"
    return render_template('home.html')


@app.route('/course')
def course():
    return render_template('course.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


@app.route('/article/<string:id>/')
def display_article(id):
    return render_template('article.html', id=id)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run(debug=True)


