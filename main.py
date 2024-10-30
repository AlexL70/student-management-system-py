from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QTableWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Studend Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        addStudentAction = file_menu_item.addAction("Add Student")
        help_menu_item = self.menuBar().addMenu("&Help")
        aboutAction = help_menu_item.addAction("About")

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Course", "Mobile"])
        self.setCentralWidget(self.table)

    def load_data(self):
        pass

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())