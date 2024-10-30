from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setWindowTitle("Age Calculator")

        # Create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        date_birth_label = QLabel("Date of Birth (MM/DD/YYYY):")
        self.date_birth_line_edit = QLineEdit()
        calc_button = QPushButton('Calculate the age')
        calc_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to the layout
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calc_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # Set the layout
        self.setLayout(grid)

    def calculate_age(self) -> None:
        now = datetime.now()
        # Get the date of birth
        try:
            date_birth = datetime.strptime(
                self.date_birth_line_edit.text(), "%m/%d/%Y")
            years = relativedelta(now, date_birth).years
        except ValueError:
            years = None
        if years is not None:
            name = self.name_line_edit.text()
            if not name:
                name = "there"
            self.output_label.setText(
                f"Hello {name}, you are {years} years old.")
        else:
            self.output_label.setText(
                "Invalid date of birth. Please enter a valid date in 'MM/DD/YYYY' format.")


# Create, initialize and run the application
app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
