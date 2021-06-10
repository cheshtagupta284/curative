'''
A resource to cater various requests from patients
# register (patient)
# get (patient)
# get (patient list)
# login
# logout
# diagnose
'''

from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt
from blacklist import BLACKLIST
from models.patient import PatientModel


class PatientRegister(Resource):
    '''
    Register a Patient
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True,type=str)
    parser.add_argument('password', required=True,type=str)
    parser.add_argument('city', required=True, type=str)
    parser.add_argument('contact', required=True, type=int)
    parser.add_argument('state', required=True, type=str)
    parser.add_argument('name', required=True, type=str)
    parser.add_argument('age', required=True, type=str)
    parser.add_argument('gender', required=True, type=str)
    parser.add_argument('date', required=True, type=str)
    def post(self):
        data = PatientRegister.parser.parse_args()
        if PatientModel.find_patient_by_email(data['email']):
            return {'message': "Email already exists."}, 400
        patient = PatientModel(**data)
        patient.save_to_db()
        return {'message': "Sign up successful"}, 201

class Patient(Resource):
    '''
    Retrieve single patient data
    '''
    def get(self, patient_id):
        patient = PatientModel.find_patient_by_id(patient_id)
        if patient: return {'patient': patient.json()}, 200
        return {'message': 'patient not found'}, 404

class PatientList(Resource):
    '''
    Retreive all patients data
    '''
    def get(self):
        return {'patients': [patient.json() for patient in PatientModel.find_all()]}, 200
