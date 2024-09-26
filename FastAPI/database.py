from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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

# Create the database tables
Base.metadata.create_all(bind=engine)
