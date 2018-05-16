import os
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.file['image']
	f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

	file.save(f)
	return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)