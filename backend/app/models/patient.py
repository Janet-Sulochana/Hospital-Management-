from app.extensions import db


class Patient(db.Model):

    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(db.String(15))

    date_of_birth = db.Column(db.Date)

    blood_group = db.Column(db.String(10))

    address = db.Column(db.Text)

    is_active = db.Column(
        db.Boolean,
        default=True
    )
    appointments = db.relationship(
        "Appointment",
        backref="patient",
        lazy=True
    )

    def __repr__(self):
        return f"<Patient {self.name}>"