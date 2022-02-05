from flask import Flask, make_response, render_template, request
app = Flask(__name__)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    resp = make_response(render_template('readcookie.html'))
    if request.method == 'POST':
     user = request.form['nm']
   
     
     resp.set_cookie('userID', user)
    return resp


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1> Olá ' + name + '</h1>'

if __name__ == '__main__':
   app.run(debug = True)

   