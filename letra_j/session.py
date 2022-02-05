from flask import Flask, render_template, session, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'administrador'

@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('index.html', username=username)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')

#python
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug = True)