'''
A resource to register doctors because doctors will be registered through an endpoint.
'''

from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt
from blacklist import BLACKLIST
from models.doctor import DoctorModel


class DoctorRegister(Resource):
    '''
    Register a doctor
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True,type=str)
    parser.add_argument('password', required=True,type=str)
    parser.add_argument('city', required=True, type=str)
    parser.add_argument('contact', required=True, type=int)
    parser.add_argument('state', required=True, type=str)
    parser.add_argument('name', required=True, type=str)
    parser.add_argument('verified', required=True, type=str)
    parser.add_argument('IMRNumber', required=True, type=int)

    def post(self):
        data = DoctorRegister.parser.parse_args()
        if DoctorModel.find_doctor_by_email(data['email']):
            return {'message': "Email already exists."}, 400
        doctor = DoctorModel(**data)
        doctor.save_to_db()
        return {'message': "Sign up successful"}, 201

class Doctor(Resource):
    '''
    Retrieve single doctor data
    '''
    def get(self, doctor_id):
        doctor = DoctorModel.find_doctor_by_id(doctor_id)
        if doctor:
            return {'doctor': doctor.json()}, 200
        return {'message': 'doctor not found'}, 404

class DoctorList(Resource):
    '''
    Retreive all doctors data
    '''
    def get(self):
        return {'doctors': [doctor.json() for doctor in DoctorModel.find_all()]}, 200