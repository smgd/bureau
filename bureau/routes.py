from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, send_from_directory
import os
from datetime import datetime

from bureau import app, db
from bureau.models import Car

def period(start_of_period, end_of_period):
    cars = Car.query.all()
    valid_cars = []

    for car in cars:
        if car.creation_date > end_of_period or car.disposal_date < start_of_period:
            # valid_cars.append(car)
            pass
        else:
            valid_cars.append(car)

    return valid_cars

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

@app.route('/<path:filename>')
def send_img(filename):  
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/choose_period', methods=['GET', 'POST'])
def choose_period():
    if request.method == 'POST':
        start_of_period = datetime.strptime(request.form['start_of_period'], '%Y-%m-%d')
        end_of_period = datetime.strptime(request.form['end_of_period'], '%Y-%m-%d')
        valid_cars = period(start_of_period, end_of_period)
        if valid_cars != []:
            return render_template('list.html', cars=valid_cars)
        else:
            return 'nooo'

    return render_template('choose_period.html')

@app.route('/list')
def list():
    return render_template('list.html', cars=Car.query.all())