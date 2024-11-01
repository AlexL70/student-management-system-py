from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox
from storage import Storage
from data_transfer_objects import Student, Courses


class EditDialog(QDialog):
    def __init__(self, student: Student) -> None:
        super().__init__()
        self.setWindowTitle("Update student data")
        self.setFixedSize(300, 300)
        self.layout = QVBoxLayout()

        self.student_id: int = student.student_id
        self.student_name = QLineEdit(student.name)
        self.student_name.setPlaceholderText("Name")
        self.layout.addWidget(self.student_name)

        self.student_course = QComboBox()
        self.student_course.setPlaceholderText("Course")
        self.student_course.addItems([course.value for course in Courses])
        self.student_course.setCurrentText(student.course)
        self.layout.addWidget(self.student_course)

        self.student_mobile = QLineEdit()
        self.student_mobile.setPlaceholderText("Mobile")
        self.student_mobile.setText(student.mobile)
        self.layout.addWidget(self.student_mobile)

        submit = QPushButton("Save changes")
        submit.clicked.connect(self.edit_student)
        self.layout.addWidget(submit)

        self.setLayout(self.layout)

    def edit_student(self) -> None:
        student = Student(
            self.student_name.text(),
            self.student_course.currentText(),
            self.student_mobile.text(),
            self.student_id)
        Storage.edit_student(student)
        self.close()
