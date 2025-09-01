import sys
import os

# Add lib/db to the Python path
sys.path.append(os.path.abspath("lib/db"))

from models import User, Door, UserDoor, AccessLog, session

print("=== Users ===")
users = session.query(User).all()
for u in users:
    print(u.id, u.name, u.role)

print("\n=== Doors ===")
doors = session.query(Door).all()
for d in doors:
    print(d.id, d.location, d.restricted)

print("\n=== User-Door Links ===")
links = session.query(UserDoor).all()
for l in links:
    print(l.user_id, l.door_id)

print("\n=== Access Logs ===")
logs = session.query(AccessLog).all()
for log in logs:
    print(log.id, log.user_id, log.door_id, log.success, log.timestamp)
