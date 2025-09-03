from lib.db import Session, engine
from lib.db.models import User, Door, AccessLog, Base
from lib.helpers import exit_program

def menu():
    print("\n--- Gatekeeper Access Control System ---")
    print("1. List Users")
    print("2. List Doors")
    print("3. Add User")
    print("4. Add Door")
    print("5. Record Access Attempt")
    print("6. Show Access Logs")
    print("0. Exit")

def main():
    session = Session()
    while True:
        menu()
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        
        elif choice == "1":  # List Users
            users = session.query(User).all()
            if not users:
                print("No users found.")
            for user in users:
                print(f"ID: {user.id} | Name: {user.name} | Role: {user.role}")
        
        elif choice == "2":  # List Doors
            doors = session.query(Door).all()
            if not doors:
                print("No doors found.")
            for door in doors:
                restricted = "Yes" if door.restricted else "No"
                print(f"ID: {door.id} | Location: {door.location} | Restricted: {restricted}")
        
        elif choice == "3":  # Add User
            name = input("User name: ")
            role = input("Role (Employee/Admin/Visitor): ")
            user = User(name=name, role=role)
            session.add(user)
            session.commit()
            print(f"Added User: {user.name} (Role: {user.role})")
        
        elif choice == "4":  # Add Door
            location = input("Door location: ")
            restricted_input = input("Restricted? (y/n): ").lower()
            restricted = True if restricted_input == "y" else False
            door = Door(location=location, restricted=restricted)
            session.add(door)
            session.commit()
            print(f"Added Door: {door.location} | Restricted: {'Yes' if restricted else 'No'}")
        
        elif choice == "5":  # Record Access Attempt
            user_id = int(input("User ID: "))
            door_id = int(input("Door ID: "))
            user = session.query(User).get(user_id)
            door = session.query(Door).get(door_id)
            if not user or not door:
                print("Invalid user or door.")
                continue
            success = door in user.doors
            log = AccessLog(user=user, door=door, success=success)
            session.add(log)
            session.commit()
            print(f"Access attempt recorded: {'Success' if success else 'Denied'}")
        
        elif choice == "6":  # Show Access Logs
            logs = session.query(AccessLog).all()
            if not logs:
                print("No access logs found.")
            for log in logs:
                status = "Success" if log.success else "Denied"
                print(f"{log.timestamp} | User: {log.user.name} | Door: {log.door.location} | {status}")
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
