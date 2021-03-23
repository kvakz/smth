from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Главная страница')

@app.route('/a')
def hello_world():
    return render_template('index2.html', title='Главная страница')

if __name__ == '__main__':
    app.run()
