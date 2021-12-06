from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class DoctorModel(db.Model):
    ''' 9 attributes in Doctor table'''
    __tablename__ = 'doctors'    
    
    IMRNumber = db.Column(db.Integer, unique=True)    
    verified = db.Column(db.String(1))
    name = db.Column(db.String(80))
    city = db.Column(db.String(20))
    state = db.Column(db.String(25))   
    password = db.Column(db.String(80))    
    contact = db.Column(db.String(10), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    date = db.Column(db.Date())
    appointments = db.relationship('AppointmentModel', lazy='dynamic', back_populates="doctors")
    specializations = db.relationship('SpecializationModel', lazy='dynamic', back_populates="doctors")

    def __init__(self, email, name, password, city, state, contact, IMRNumber, verified, date):
        self.email = email
        self.name = name
        self.contact = contact
        self.IMRNumber = IMRNumber
        self.city = city
        self.verified = verified
        self.password = generate_password_hash(password)
        self.state = state
        format_str = '%Y-%m-%d' # The format
        datetime_obj = datetime.strptime(date, format_str)
        self.date = datetime_obj.date()

    def json(self):
        # A method to return the json of single doctor data using object
        return {'id': self.id,
                'state': self.state,
                'email': self.email,
                'name': self.name,
                "password": self.password,
                'IMRNumber': self.IMRNumber,
                'verified': self.verified,
                'city': self.city,
                'contact': self.contact,
                'date' : str(self.date)
                }

    def save_to_db(self):
        # A method to save single doctor data to the database permanently
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # A method to delete single doctor data from the database permanently
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_all(cls):
        # A mapping to retreive all doctor data from the database
        return cls.query.all()

    @classmethod
    def find_doctor_by_email(cls, email):        
        # A mapping to retreive single doctor data from the database using email
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_doctor_by_id(cls, _id):
        # A mapping to retreive single doctor data from the database using id
        return cls.query.filter_by(id=_id).first()
