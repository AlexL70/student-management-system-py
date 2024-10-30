from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton


class SearchByNameDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Search by Name")
        self.setFixedSize(300, 200)
        self.layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        self.layout.addWidget(self.student_name)

        submit = QPushButton("Search")
        submit.clicked.connect(self.search_student_by_name)
        self.layout.addWidget(submit)

        self.setLayout(self.layout)

    def search_student_by_name(self) -> None:
        """Search student by name."""
        self.close()
