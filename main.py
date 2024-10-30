from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QTableWidget
import sys
import os
import sqlite3


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
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Course", "Mobile"])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        data = connection.execute("SELECT * FROM students")
        for row_num, row_data in enumerate(data):
            self.table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(
                    row_num, col_num, QTableWidgetItem(str(col_data)))
        connection.close()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
