from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import os

from bureau import app, db
from bureau.models import Car
from bureau.forms import SubmitForm

# print(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmitForm(request.form)
    
    if request.method == 'POST' and form.validate():
        print(app.config['UPLOAD_FOLDER'])
        filename = form.scan.data.filename
        f = form.scan.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('index.html', form=form)