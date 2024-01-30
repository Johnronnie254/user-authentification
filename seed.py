# seed.py
from app import app  # Assuming your Flask app instance is named 'app'
from models import db, Users

# Create tables (if not already created)
with app.app_context():
    db.create_all()

    # Seed data: Generate and add 10 users
    for i in range(1, 11):
        username = f'user{i}'
        password = f'password{i}'

        new_user = Users(username=username, password=password)
        db.session.add(new_user)

    # Commit the changes to the database
    db.session.commit()

    print("Seed data added successfully.")
