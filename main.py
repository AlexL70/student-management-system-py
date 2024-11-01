from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QTableWidget, QToolBar
from PyQt6.QtGui import QAction, QIcon
import sys

from add_student_dialog import AddStudentDialog
from search_by_name_dialog import SearchByNameDialog
from storage import Storage


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Studend Management System")
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        add_student_action = QAction(
            QIcon("icons/add.png"), "Add Student", self)
        file_menu_item.addAction(add_student_action)
        add_student_action.triggered.connect(self.add_student)
        edit_menu_item = self.menuBar().addMenu("&Edit")
        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search_by_name)
        help_menu_item = self.menuBar().addMenu("&Help")
        about_action = help_menu_item.addAction("About")

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Course", "Mobile"])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create a toolbar and add buttons to it
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

    def load_data(self) -> None:
        data = Storage.load_data()
        for row_num, row_data in enumerate(data):
            self.table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(
                    row_num, col_num, QTableWidgetItem(str(col_data)))

    def add_student(self) -> None:
        dialog = AddStudentDialog()
        dialog.exec()
        self.table.clear()
        self.load_data()

    def search_by_name(self) -> None:
        dialog = SearchByNameDialog()
        dialog.exec()
        rows = dialog.data
        items = self.table.findItems(
            dialog.name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            self.table.item(item.row(), 1).setSelected(True)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
