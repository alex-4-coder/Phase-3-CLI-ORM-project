from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# Many-to-Many association table
user_door = Table(
    'user_door', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('door_id', Integer, ForeignKey('doors.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, default='Employee')

    doors = relationship('Door', secondary=user_door, back_populates='users')
    access_logs = relationship('AccessLog', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, role={self.role})>"

class Door(Base):
    __tablename__ = 'doors'
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    restricted = Column(Boolean, default=True)

    users = relationship('User', secondary=user_door, back_populates='doors')
    access_logs = relationship('AccessLog', back_populates='door')

    def __repr__(self):
        return f"<Door(id={self.id}, location={self.location}, restricted={self.restricted})>"

class AccessLog(Base):
    __tablename__ = 'access_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    door_id = Column(Integer, ForeignKey('doors.id'))
    success = Column(Boolean)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='access_logs')
    door = relationship('Door', back_populates='access_logs')

    def __repr__(self):
        return f"<AccessLog(user={self.user.name}, door={self.door.location}, success={self.success}, time={self.timestamp})>"
