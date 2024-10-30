import sqlite3


class Student:
    def __init__(self, name: str, course: str, mobile: str) -> None:
        self.name = name
        self.course = course
        self.mobile = mobile


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
