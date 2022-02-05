import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload')


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      savePath = os.path.join(UPLOAD_FOLDER,secure_filename(f.filename))
      f.save(savePath)
      return 'upload feito com sucesso'
		
if __name__ == '__main__':
   app.run(debug = True)