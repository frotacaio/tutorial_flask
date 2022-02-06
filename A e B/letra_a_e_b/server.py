############################################################################################
#Flask é um framework web, é um módulo Python que permite desenvolver aplicações web facilmente. Ele tem um núcleo pequeno e fácil de estender: é um microframework que não inclui um ORM (Object Relational Manager) ou recursos semelhantes. Ele tem muitos recursos interessantes, como roteamento de URL, mecanismo de modelo. É uma estrutura de aplicativo da web WSGI.

############################################################################################

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Letra A e B - Hello Word'

app.run(host='0.0.0.0', port=81)

#A e B