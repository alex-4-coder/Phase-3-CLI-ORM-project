# lib/debug.py

from db.models import Base, User, Door, AccessLog, engine, Session
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Create a new session
session = Session()

def create_test_users(n=3):
    """Create n test users with random names and roles."""
    users = [User(name=fake.name(), role=random.choice(['Employee', 'Admin', 'Visitor'])) for _ in range(n)]
    session.add_all(users)
    session.commit()
    print(f"Created {n} users:")
    for u in users:
        print(u)
    return users

def create_test_doors(n=2):
    """Create n test doors with random locations."""
    doors = [Door(location=fake.street_name()) for _ in range(n)]
    session.add_all(doors)
    session.commit()
    print(f"Created {n} doors:")
    for d in doors:
        print(d)
    return doors

def assign_access(users, doors):
    """Randomly assign users access to doors (many-to-many)."""
    for user in users:
        user.doors = random.sample(doors, random.randint(1, len(doors)))
    session.commit()
    print("Assigned doors to users:")
    for u in users:
        print(f"{u.name} can access: {[door.location for door in u.doors]}")

def create_access_logs(users, doors, n=5):
    """Create random access logs for users and doors."""
    logs = []
    for _ in range(n):
        user = random.choice(users)
        door = random.choice(doors)
        success = door in user.doors
        log = AccessLog(user=user, door=door, success=success)
        session.add(log)
        logs.append(log)
    session.commit()
    print("Created access logs:")
    for log in logs:
        print(log)

# Example of using debug functions
if __name__ == "__main__":
    users = create_test_users(5)
    doors = create_test_doors(3)
    assign_access(users, doors)
    create_access_logs(users, doors, 10)
