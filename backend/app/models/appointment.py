from datetime import datetime
from app.extensions import db


class Appointment(db.Model):

    __tablename__ = "appointments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )

    appointment_date = db.Column(
        db.Date,
        nullable=False
    )

    appointment_time = db.Column(
        db.Time,
        nullable=False
    )

    reason = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="scheduled"
    )

    booked_on = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    medical_record = db.relationship(
        "MedicalRecord",
        backref="appointment",
        uselist=False
    )

    bill = db.relationship(
        "Bill",
        backref="appointment",
        uselist=False
    )
    def __repr__(self):
        return f"<Appointment {self.id}>"