import sqlite3
from data_transfer_objects import Student


class Storage:
    @staticmethod
    def __get_connection():
        return sqlite3.connect("database.db")

    @staticmethod
    def load_data() -> list:
        connection = Storage.__get_connection()
        cursor = connection.execute("SELECT * FROM students")
        data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def add_student(student: Student) -> None:
        connection = Storage.__get_connection()
        connection.cursor().execute(
            "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
            (student.name, student.course, student.mobile))
        connection.commit()
        connection.close()

    @staticmethod
    def edit_student(student: Student) -> None:
        connection = Storage.__get_connection()
        connection.cursor().execute(
            "UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
            (student.name, student.course, student.mobile, student.student_id))
        connection.commit()
        connection.close()

    @staticmethod
    def search_by_name(name: str) -> list:
        connection = Storage.__get_connection()
        cursor = connection.cursor().execute(
            "SELECT * FROM students WHERE name = ?", (name,))
        data = cursor.fetchall()
        connection.close()
        return data
