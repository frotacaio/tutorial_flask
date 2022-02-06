from flask import Flask, render_template, request, redirect, url_for
# Initialize the Flask application
app = Flask(__name__)
 
 
@app.route('/')
def index():
   return render_template('log_in.html')
    
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['txtemail'] == 'caiofrota@gmail.com' and request.form['txtpass'] == 'secreto012' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('errorlogin'))
 
@app.route('/success')
def success():
   return '<h1>Logado com sucesso</h1>'
  
@app.route('/errorlogin')
def errorlogin():
   return '<h1>Credenciais erradas, tente novamente <a href = "/">login</a></h1>'
    
if __name__ == '__main__':
   app.run(debug = True)