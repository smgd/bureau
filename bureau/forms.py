from wtforms import Form, StringField, DateField, FileField, validators
from flask_wtf.file import FileRequired

class SubmitForm(Form):
    vin = StringField('VIN', [validators.Length(min=17, max=17)])
    scan = FileField('Scan', validators=[FileRequired()])
    creation_date = DateField('Creation Date', format='%Y-%m-%d')
    disposal_date = DateField('Disposal Date', format='%Y-%m-%d')
