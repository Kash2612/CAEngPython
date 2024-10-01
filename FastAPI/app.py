from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Student
from routers import authentication

app = FastAPI()

app.include_router(authentication.router)

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a student with subjects
@app.post("/students")
def create_student(
        name: str,
        age: int,
        subject1_name: str,
        subject1_marks: int,
        subject2_name: str = None,
        subject2_marks: int = None,
        subject3_name: str = None,
        subject3_marks: int = None,
        db: Session = Depends(get_db),
):
    db_student = Student(
        name=name,
        age=age,
        subject1_name=subject1_name,
        subject1_marks=subject1_marks,
        subject2_name=subject2_name,
        subject2_marks=subject2_marks,
        subject3_name=subject3_name,
        subject3_marks=subject3_marks,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {
        "id": db_student.id,
        "name": db_student.name,
        "age": db_student.age,
        "subjects": [
            {"name": db_student.subject1_name, "marks": db_student.subject1_marks},
            {"name": db_student.subject2_name, "marks": db_student.subject2_marks},
            {"name": db_student.subject3_name, "marks": db_student.subject3_marks},
        ],
    }


# Read a student by ID
@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {
        "id": db_student.id,
        "name": db_student.name,
        "age": db_student.age,
        "subjects": [
            {"name": db_student.subject1_name, "marks": db_student.subject1_marks},
            {"name": db_student.subject2_name, "marks": db_student.subject2_marks},
            {"name": db_student.subject3_name, "marks": db_student.subject3_marks},
        ],
    }



# Update a student
@app.put("/students/{student_id}")
def update_student(
        student_id: int,
        name: str,
        age: int,
        subject1_name: str,
        subject1_marks: int,
        subject2_name: str = None,
        subject2_marks: int = None,
        subject3_name: str = None,
        subject3_marks: int = None,
        db: Session = Depends(get_db),
):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db_student.name = name
    db_student.age = age
    db_student.subject1_name = subject1_name
    db_student.subject1_marks = subject1_marks
    db_student.subject2_name = subject2_name
    db_student.subject2_marks = subject2_marks
    db_student.subject3_name = subject3_name
    db_student.subject3_marks = subject3_marks

    db.commit()
    db.refresh(db_student)
    return db_student


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()
    return db_student