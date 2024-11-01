from enum import Enum
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

from storage import Storage, Student


class Courses(Enum):
    BIOLOGY = "Biology"
    MATH = "Math"
    ASTRONOMY = "Astronomy"
    PHYSICS = "Physics"
    PYTHON = "Python"


class AddStudentDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Add Student")
        self.setFixedSize(300, 300)
        self.layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        self.layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        self.course_name.setPlaceholderText("Course")
        self.course_name.addItems([course.value for course in Courses])
        self.layout.addWidget(self.course_name)

        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Mobile")
        self.layout.addWidget(self.mobile_number)

        submit = QPushButton("Register")
        submit.clicked.connect(self.add_student)
        self.layout.addWidget(submit)

        self.setLayout(self.layout)

    def add_student(self) -> None:
        student = Student(
            self.student_name.text(),
            self.course_name.currentText(),
            self.mobile_number.text())
        Storage.add_student(student)
        self.close()
