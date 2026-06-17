from datetime import datetime
from app.extensions import db


class MedicalRecord(db.Model):

    __tablename__ = "medical_records"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    appointment_id = db.Column(
        db.Integer,
        db.ForeignKey("appointments.id"),
        nullable=False,
        unique=True
    )

    diagnosis = db.Column(db.Text)

    prescription = db.Column(db.Text)

    notes = db.Column(db.Text)

    recorded_on = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    def __repr__(self):
        return f"<MedicalRecord {self.id}>"