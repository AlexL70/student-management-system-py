from data_transfer_objects import Student
import mysql.connector
import os


class Storage:
    @staticmethod
    def __get_connection() -> mysql.connector.MySQLConnection:
        host = os.getenv("MYSQL_DB_HOST")
        port = os.getenv("MYSQL_DB_PORT")
        user = os.getenv("MYSQL_DB_USER")
        password = os.getenv("MYSQL_DB_PASSWORD")
        database = os.getenv("MYSQL_SCHOOL_DATABASE")
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database)

    @staticmethod
    def load_data() -> list:
        connection = Storage.__get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def add_student(student: Student) -> None:
        connection = Storage.__get_connection()
        connection.cursor().execute(
            "INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
            (student.name, student.course, student.mobile))
        connection.commit()
        connection.close()

    @staticmethod
    def edit_student(student: Student) -> None:
        connection = Storage.__get_connection()
        connection.cursor().execute(
            "UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
            (student.name, student.course, student.mobile, student.student_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete_student(student: Student) -> None:
        connection = Storage.__get_connection()
        connection.cursor().execute(
            "DELETE FROM students WHERE id = %s", (student.student_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def search_by_name(name: str) -> list:
        connection = Storage.__get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE name = %s", (name,))
        data = cursor.fetchall()
        connection.close()
        return data
