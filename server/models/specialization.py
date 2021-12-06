from db import db
from datetime import datetime

class SpecializationModel(db.Model):
    __tablename__ = 'specializations'    
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    doctorID = db.Column(db.Integer,db.ForeignKey('doctors.id'))
    doctors = db.relationship('DoctorModel', back_populates="specializations")

    def __init__(self, name, doctorID):
        self.doctorID = doctorID
        self.name = name

    def json(self):
        # A method to return the json of single specialization data using object
        return {
                'doctorID': self.doctorID,
                'name': self.name,
                }

    def save_to_db(self):
        # A method to save single specialization data to the database permanently
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # A method to delete single specialization data from the database permanently
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_all(cls):
        # A mapping to retreive all specialization data from the database
        return cls.query.all()

    @classmethod
    def find_specialization_by_email(cls, email):        
        # A mapping to retreive single specialization data from the database using email
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_specialization_by_id(cls, _id):
        # A mapping to retreive single specialization data from the database using id
        return cls.query.filter_by(id=_id).first()
