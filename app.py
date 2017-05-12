import os
from flask import *
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '\\uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['txt','jpg','jpeg','png','mp3','mp4','avi','mkv'])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/upload',methods=['POST'])
def upload():
	if request.method=='POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.getcwd()+app.config['UPLOAD_FOLDER']+'\\'+filename)
		return redirect(url_for('success'))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')