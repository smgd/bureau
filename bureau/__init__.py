from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='../templates')

app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'files')

db = SQLAlchemy(app)

from bureau.models import Car

# if not os.path.exists(os.path.join(os.getcwd(), 'cars.db')):
#     db.create_all()

from bureau import routes