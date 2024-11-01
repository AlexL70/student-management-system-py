from enum import Enum


class Courses(Enum):
    BIOLOGY = "Biology"
    MATH = "Math"
    ASTRONOMY = "Astronomy"
    PHYSICS = "Physics"
    PYTHON = "Python"


class Student:
    def __init__(self, name: str, course: str, mobile: str, studend_id: int = None) -> None:
        self.name: str = name
        self.course: str = course
        self.mobile: str = mobile
        if studend_id:
            self.student_id: int = studend_id
