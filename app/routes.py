from flask import Flask, request, render_template, redirect, send_file
from app import app, counter
from app.forms import MyForm
from werkzeug.utils import secure_filename
import os

import uuid

@app.route('/')
@app.route('/index')
def index():
    text = "Классный сайт ЙУЮХУУУ"
    countries = {'Russia': 'Moscow', 'Italy': 'Rome', 'Finland': 'Oslo'}
    return render_template('index.html', title=text, data=countries)
@app.route('/template')
def lol():
    return render_template('index.html', name="lol")

@app.route('/upload', methods = ['GET','POST'])
def upload():
    form = MyForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = str(uuid.uuid4())[:5]+'.'+f.filename.split('.')[-1]
        print(filename) 
        if(os.path.exists(os.path.join(os.getcwd(), 'app', 'files'))):
            f.save(os.path.join(os.getcwd(), 'app', 'files', filename))
            with open(os.path.join(os.getcwd(), 'app', 'files', filename), 'r') as f_:
                data = counter.count_letters_RU(f_.read())
                print(data)
                counter.make_letters_hist(data, os.path.join(os.getcwd(), 'app', 'files', filename.split('.')[0]))
            
            return render_template('index.html', fname=str(f.filename), data = data, imgname = filename.split('.')[0])
        else:
            return render_template('upload.html', form=form)
        
    return render_template('upload.html', form=form)
    
@app.route('/getimage/<name>')
def get_image(name):
    if(os.path.isfile(os.path.join(os.getcwd(), 'app', 'files', name+'.png'))):
        return send_file(os.path.join(os.getcwd(), 'app', 'files', name+'.png'), mimetype='image/png')
    return False