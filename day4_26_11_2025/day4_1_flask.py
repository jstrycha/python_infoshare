from markupsafe import escape
from flask import Flask, render_template, request, url_for

app = Flask(__name__) # __name__ - nazwa pliku
#app = Flask(__name__, template_folder='views') - zmiana folderu skąd są brane tempatki

# @app.route('/') # pod jakim adresem będzie ta funkcja dostępna
# def hello():
#     return 'Hello World!'

# @app.route('/') # wywoła się tylko metoda hello(), hi() już nie, bo nie da się 2 razy pdo tego samego route'a
# def hi():
#     return 'Hello World again!'

# @app.route('/hi')
# @app.route('/hi/<name>')
# def hi(name='Kopytko'):
#     return escape('<h1>Hi {0}</h1>'.format(name))

# @app.route('/hi')
# @app.route('/hi/<path:name>')
# def hi(name='kopytko'):
#     return render_template('hi.html', t_name=name) # render_template ma wbudowanego escape'a

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hi')
@app.route('/hi/<path:name>')
def hi_get(name='kopytko'):
    return render_template('hi.html', t_name=name)

@app.route('/hi_for_ai', methods = ['POST'])
def hi_post():
    # request.method
    name = request.form['first_name']
    age = request.form['age']
    return render_template('hi.html', t_name=name, t_age=age)

app.run(debug=True) # wywołanie aplikacji