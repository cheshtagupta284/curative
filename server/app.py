from flask import Flask
from flask_restful import Api
from resources.patient import PatientRegister, PatientList ,Patient #, PatientLogout, PatientRequest, PatientLogin
from resources.doctor import DoctorRegister, DoctorList, Doctor #, DoctorLogout, DoctorRequest, DoctorLogin
from blacklist import BLACKLIST

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# To create a database
@app.before_first_request
def create_tables():
    db.create_all()

# API resources
api.add_resource(PatientRegister, '/register/patient')
api.add_resource(PatientList, '/patients')
api.add_resource(Patient, '/patient/<int:patient_id>')
api.add_resource(DoctorRegister, '/register/doctor')
api.add_resource(DoctorList, '/doctors')
api.add_resource(Doctor, '/doctor/<int:doctor_id>')

# Run the app
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
