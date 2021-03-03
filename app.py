from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/articles/<int:article_id>')
def about(article_id):
    return render_template('article.html')


if __name__ == '__main__':
    app.run()
