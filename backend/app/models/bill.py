from datetime import datetime
from app.extensions import db


class Bill(db.Model):

    __tablename__ = "bills"

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

    consultation_fee = db.Column(
        db.Float,
        default=0.0
    )

    additional_charges = db.Column(
        db.Float,
        default=0.0
    )

    total_amount = db.Column(
        db.Float,
        default=0.0
    )

    payment_status = db.Column(
        db.String(20),
        default="unpaid"
    )

    billed_on = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    def __repr__(self):
        return f"<Bill {self.id}>"