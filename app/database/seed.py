from app.database.connection import SessionLocal
from app.models.user import User


db = SessionLocal()

users = [
    User(name="Abi", email="abi@gmail.com"),
    User(name="John", email="john@gmail.com"),
    User(name="Priya", email="priya@gmail.com"),
]

db.add_all(users)
db.commit()
db.close()

print("Users inserted successfully")