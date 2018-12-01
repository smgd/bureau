from bureau import db

class Car(db.Model):
    id = db.Column(db.String(17), primary_key=True, autoincrement=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    disposal_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Car('{self.id}', '{self.scan}', '{self.creation_date}', '{self.disposal_date}')"