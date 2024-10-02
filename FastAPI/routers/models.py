from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    subject1_name = Column(String)
    subject1_marks = Column(Integer)
    subject2_name = Column(String)
    subject2_marks = Column(Integer)
    subject3_name = Column(String)
    subject3_marks = Column(Integer)
