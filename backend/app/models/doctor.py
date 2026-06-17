from app.extensions import db

class Doctor(db.Model):

    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    specialization = db.Column(db.String(100))

    qualification = db.Column(db.String(100))

    experience_years = db.Column(db.Integer)

    availability_days = db.Column(db.String(100))

    is_active = db.Column(
        db.Boolean,
        default=True
    )
    appointments = db.relationship(
    "Appointment",
    backref="doctor",
    lazy=True
)
    def __repr__(self):
         return f"<Department {self.name}>"