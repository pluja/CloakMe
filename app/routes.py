from flask import render_template, flash, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app
import subprocess
import uuid 
import os

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.referrer)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.referrer)
        if file:
            folder = str(uuid.uuid1())
            os.mkdir('app/'+folder)
            fileName = cloak(file, folder)            
            return send_from_directory(folder, fileName, as_attachment=True)
    else:
        return render_template('index.html')

def cloak(file, folder):
    file.save(os.path.join('app/'+folder, file.filename))
    args = ("bin/fawkes", "--directory", 'app/'+folder)
    #Or just:
    #args = "bin/bar -c somefile.xml -d text.txt -r aString -f anotherString".split()
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    cloakedFile = file.filename.split(".")[0]+"_min_cloaked.png"
    return cloakedFile