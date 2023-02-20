'''
You can handle uploaded files with Flask easily. 
Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.
'''
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        _file = request.files['the_file']
        _file.save(f'./{secure_filename(_file.filename)}')
        error = 'success'
    else:
        error = 'Failed'
    return error
