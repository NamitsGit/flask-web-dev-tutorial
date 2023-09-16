from . import db
from datetime import date

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    sex = db.Column(db.String(1), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    regd_phone_no = db.Column(db.String(15), unique=True, nullable=False)
    regd_email = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return "<{}, {}, {}, {}, {}, {}, {}>".format(self.id, self.first_name, self.last_name, self.sex, self.dob, self.regd_phone_no, self.regd_email)
