from db import db
from datetime import datetime

class MedicineModel(db.Model):
    __tablename__ = 'medicines'    
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    medicalHistoryID = db.Column(db.Integer, db.ForeignKey('medicalHistory.id'))
    medicalHistory = db.relationship('MedicalHistoryModel', back_populates="medicines")

    def __init__(self, name, medicalHistoryID):
        self.medicalHistoryID = medicalHistoryID
        self.name = name

    def json(self):
        # A method to return the json of single medicine data using object
        return {
                'medicalHistoryID': self.medicalHistoryID,
                'name': self.name,
                }

    def save_to_db(self):
        # A method to save single medicine data to the database permanently
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # A method to delete single medicine data from the database permanently
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_all(cls):
        # A mapping to retreive all medicine data from the database
        return cls.query.all()

    @classmethod
    def find_medicine_by_email(cls, email):        
        # A mapping to retreive single medicine data from the database using email
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_medicine_by_id(cls, _id):
        # A mapping to retreive single medicine data from the database using id
        return cls.query.filter_by(id=_id).first()
