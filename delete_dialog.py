from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QMessageBox

from data_transfer_objects import Student
from storage import Storage


class DeleteDialog(QDialog):
    def __init__(self, student: Student) -> None:
        super().__init__()
        self.setWindowTitle("Delete student")
        self.setFixedSize(500, 200)

        self.student = student

        layout = QGridLayout()
        confirmation = QLabel(
            f"Are you sure you want to delete \"{student.name}\"?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)
        no.clicked.connect(self.close)

    def delete_student(self) -> bool:
        Storage.delete_student(self.student)
        super().close()
        QMessageBox().information(self, "Success", "Student deleted successfully")

    def close(self) -> None:
        super().close()
