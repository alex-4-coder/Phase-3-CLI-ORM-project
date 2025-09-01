from db.seed import Session, engine
from db.models import User, Door, AccessLog
from helpers import exit_program

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
        elif choice == "1":
            for u in session.query(User).all():
                print(u)
        elif choice == "2":
            for d in session.query(Door).all():
                print(d)
        elif choice == "3":
            name = input("User name: ")
            role = input("Role (Employee/Admin/Visitor): ")
            user = User(name=name, role=role)
            session.add(user)
            session.commit()
            print(f"Added {user}")
        elif choice == "4":
            location = input("Door location: ")
            door = Door(location=location)
            session.add(door)
            session.commit()
            print(f"Added {door}")
        elif choice == "5":
            user_id = int(input("User ID: "))
            door_id = int(input("Door ID: "))
            user = session.query(User).get(user_id)
            door = session.query(Door).get(door_id)
            if not user or not door:
                print("Invalid user or door")
                continue
            success = door in user.doors
            log = AccessLog(user=user, door=door, success=success)
            session.add(log)
            session.commit()
            print(f"Access attempt recorded: {'Success' if success else 'Denied'}")
        elif choice == "6":
            for log in session.query(AccessLog).all():
                print(log)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
