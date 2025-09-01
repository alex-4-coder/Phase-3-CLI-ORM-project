from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Door, AccessLog
from faker import Faker
import random

engine = create_engine('sqlite:///gatekeeper.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# Create Users
users = [User(name=fake.name(), role=random.choice(['Employee', 'Admin', 'Visitor'])) for _ in range(5)]
session.add_all(users)

# Create Doors
doors = [Door(location=fake.street_name()) for _ in range(3)]
session.add_all(doors)
session.commit()

# Assign Users to Doors (many-to-many)
for user in users:
    user.doors = random.sample(doors, random.randint(1, 3))
session.commit()

# Create Access Logs
for _ in range(10):
    user = random.choice(users)
    door = random.choice(doors)
    log = AccessLog(user=user, door=door, success=random.choice([True, False]))
    session.add(log)
session.commit()
print("Database seeded!")
