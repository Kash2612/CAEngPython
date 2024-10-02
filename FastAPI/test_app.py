import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import create_student, read_student, update_student, delete_student
from database import Student


# Mock the Session object from SQLAlchemy
@pytest.fixture
def mock_db_session():
    """Create a mock database session"""
    db = MagicMock(spec=Session)
    return db


def test_create_student(mock_db_session):
    # Input data for creating a student
    data = {
        "name": "John Doe",
        "age": 20,
        "subject1_name": "Math",
        "subject1_marks": 85,
        "subject2_name": "Physics",
        "subject2_marks": 90,
        "subject3_name": "Chemistry",
        "subject3_marks": 88
    }

    # Mock the add and commit methods
    mock_db_session.add = MagicMock()
    mock_db_session.commit = MagicMock()

    # Mock the refresh method to simulate returning a new student
    mock_db_session.refresh = MagicMock()

    # Call the create_student function
    response = create_student(**data, db=mock_db_session)

    # Assert that the student was added to the database session
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()

    # Validate the response
    assert response["name"] == data["name"]
    assert response["age"] == data["age"]
    assert response["subjects"][0]["name"] == data["subject1_name"]


def test_read_student(mock_db_session):
    # Mock a student instance
    student = Student(
        id=1,
        name="Jane Doe",
        age=21,
        subject1_name="Biology",
        subject1_marks=75,
        subject2_name="Chemistry",
        subject2_marks=80,
        subject3_name="Math",
        subject3_marks=90
    )

    # Mock the query and filter call
    mock_db_session.query().filter().first.return_value = student

    # Call the read_student function
    response = read_student(student.id, db=mock_db_session)

    # Validate the response
    assert response["name"] == student.name
    assert response["age"] == student.age
    assert response["subjects"][0]["name"] == student.subject1_name


def test_update_student(mock_db_session):
    # Mock an existing student
    student = Student(
        id=1,
        name="Tom Smith",
        age=22,
        subject1_name="English",
        subject1_marks=70,
        subject2_name="History",
        subject2_marks=85,
        subject3_name="Math",
        subject3_marks=78
    )

    # Mock the query and filter call
    mock_db_session.query().filter().first.return_value = student

    # Input data for updating the student
    updated_data = {
        "name": "Tom Smith Updated",
        "age": 23,
        "subject1_name": "English",
        "subject1_marks": 75,
        "subject2_name": "History",
        "subject2_marks": 90,
        "subject3_name": "Math",
        "subject3_marks": 82
    }

    # Call the update_student function
    response = update_student(student.id, db=mock_db_session, **updated_data)

    # Assert that the student was updated
    assert response.name == updated_data["name"]
    assert response.age == updated_data["age"]
    assert response.subject1_name == updated_data["subject1_name"]


def test_delete_student(mock_db_session):
    # Mock an existing student
    student = Student(
        id=1,
        name="Lucy Adams",
        age=19,
        subject1_name="Geography",
        subject1_marks=88,
        subject2_name="History",
        subject2_marks=84,
        subject3_name="English",
        subject3_marks=79
    )

    # Mock the query and filter call
    mock_db_session.query().filter().first.return_value = student

    # Call the delete_student function
    response = delete_student(student.id, db=mock_db_session)

    # Assert that the student was deleted
    mock_db_session.delete.assert_called_once_with(student)
    mock_db_session.commit.assert_called_once()

    # Check that the student no longer exists
    with pytest.raises(Exception):
        read_student(student.id, db=mock_db_session)
