from app.extensions import db

class Department(db.Model):

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    location = db.Column(db.String(100))
    
    doctors = db.relationship(
    "Doctor",
    backref="department",
    lazy=True
    )
    def __repr__(self):
        return f"<Department {self.name}>"