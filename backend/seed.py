from app import create_app
from app.extensions import db
from app.models.admin import Admin

app = create_app()

with app.app_context():

    existing_admin = Admin.query.filter_by(
        email="admin@hospital.com"
    ).first()

    if not existing_admin:

        admin = Admin(
            email="admin@hospital.com",
            password_hash="Admin@123"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created!")

    else:
        print("Admin already exists!")