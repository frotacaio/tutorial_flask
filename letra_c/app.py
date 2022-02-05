from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = ['Caio', 'Arnaldo', 'Fernando']
    return render_template('index.html',title='Bem vindo', members=users) 

app.run()