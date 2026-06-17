from flask import Flask
from app.extensions import db
from app.models.department import Department
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.models.medicalrecord import MedicalRecord
from app.models.bill import Bill
from app.models.admin import Admin
from app import models
from flask_migrate import Migrate

migrate = Migrate()

def create_app():


    app = Flask(__name__)

    app.config.from_object("config.Config")


    db.init_app(app)

    migrate.init_app(app, db)
    return app