from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import os
from datetime import datetime

from bureau import app, db
from bureau.models import Car

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        scan = request.files['scan']
        vin = request.form['vin']
        creation_date = datetime.strptime(request.form['creation_date'], '%Y-%m-%d')
        disposal_date = datetime.strptime(request.form['disposal_date'], '%Y-%m-%d')
        scan.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{vin}.jpg"))

        car = Car(id=vin, scan=f"{vin}.jpg", creation_date=creation_date, disposal_date=disposal_date)
        db.session.add(car)
        db.session.commit()
        return 'success!'

    return render_template('index.html')