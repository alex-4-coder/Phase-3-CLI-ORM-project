# Phase-3-CLI-ORM-project

# Phase-3-CLI-ORM-project

This project is a **Gatekeeper Access Control System** built with Python, SQLAlchemy ORM, and Alembic.  
It manages users, doors, access permissions, and logs every access attempt.

---

## Features

- **User Management:** Add, list, and manage users with roles (`Employee`, `Admin`, `Visitor`).
- **Door Management:** Register doors and mark them as restricted or unrestricted.
- **User-Door Relationships:** Assign which users can access which doors (many-to-many).
- **Access Logs:** Log every access attempt with timestamp, user, door, and success/failure status.
- **Database Migrations:** Use Alembic for schema versioning and upgrades.
- **Debug/Seed Utilities:** Quickly populate the database with test data.

---

## Tech Stack

- **Python 3.12**
- **SQLite** – Lightweight relational database.
- **SQLAlchemy ORM** – Object-relational mapper.
- **Alembic** – Database migrations.
- **Faker** – Generate fake data for testing.

---

## Project Structure & File Overview

```
check_db.py
gatekeeper.db
Pipfile
Pipfile.lock
README.md
db_files/
    gatekeeper.db
lib/
    cli.py
    debug.py
    helpers.py
    db/
        _init_.py
        alembic.ini
        gatekeeper.db
        models.py
        seed.py
        migrations/
            env.py
            README
            script.py.mako
            versions/
                0addc87a448a_create_tables.py
                59153c0b834c_create_tables.py
```

### Top-Level Files

- **README.md** – This documentation file.
- **Pipfile / Pipfile.lock** – Python dependencies for the project.
- **gatekeeper.db** – Main SQLite database file.
- **check_db.py** – Script to inspect and print database contents (users, doors, links, logs).

### `lib/` Directory

- **cli.py**  
  Main command-line interface for interacting with the system.  
  - Presents a menu to list/add users and doors, record access attempts, and show logs.
  - Uses SQLAlchemy sessions to interact with the database.
  - Calls [`exit_program`](lib/helpers.py) to exit.

- **debug.py**  
  Utility for quickly generating test data.  
  - Creates random users and doors.
  - Assigns access permissions.
  - Generates access logs.
  - Useful for development and debugging.

- **helpers.py**  
  Contains helper functions, e.g., `exit_program()` to cleanly exit the CLI.

#### `lib/db/` Subdirectory

- **_init_.py**  
  Initializes the database connection and session.  
  - Sets up SQLAlchemy engine and sessionmaker.
  - Imports models so they are registered.

- **models.py**  
  Defines ORM models for the system:  
  - `User`: Represents a user with name and role.
  - `Door`: Represents a door with location and restriction status.
  - `AccessLog`: Logs each access attempt.
  - `user_door`: Association table for many-to-many user-door relationships.

- **seed.py**  
  Seeds the database with random test data using Faker.  
  - Adds users, doors, assigns access, and creates access logs.

- **gatekeeper.db**  
  SQLite database file (may be a copy or backup).

#### `lib/db/migrations/` (Alembic Migrations)

- **alembic.ini**  
  Alembic configuration file (database URL, migration script location, logging).

- **env.py**  
  Alembic environment setup.  
  - Configures migration context and metadata.

- **README**  
  Notes about migration configuration.

- **script.py.mako**  
  Template for new Alembic migration scripts.

- **versions/**  
  Contains migration scripts:
  - `0addc87a448a_create_tables.py`: Initial migration, creates tables.
  - `59153c0b834c_create_tables.py`: Subsequent migration (currently empty).

---

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd Phase-3-CLI-ORM-project
    ```

2. **Install dependencies**
    ```bash
    pip install pipenv
    pipenv install
    pipenv shell
    ```

3. **Initialize the database**
    - Run Alembic migrations:
      ```bash
      cd lib/db
      alembic upgrade head
      ```
    - Or seed with test data:
      ```bash
      python lib/db/seed.py
      ```

4. **Run the CLI**
    ```bash
    python lib/cli.py
    ```

5. **Debug/Test**
    - Generate random test data:
      ```bash
      python lib/debug.py
      ```
    - Inspect database contents:
      ```bash
      python check_db.py
      ```

---

## How It Works

- **Users** can be added with a name and role.
- **Doors** can be registered with a location and restriction status.
- **Access** is managed by assigning users to doors.
- **Access Logs** record every attempt to open a door, noting if it was successful.
- **Migrations** keep the database schema up to date as models change.

---

## Contributing

Feel free to fork and submit pull requests.  
For questions, open an issue.

---

##