show databases;
CREATE DATABASE school;
SHOW TABLES FROM school;
USE school;
GRANT ALL PRIVILEGES ON school.* TO 'alexl70';
CREATE TABLE students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255),
course VARCHAR(255),
mobile VARCHAR(255));
SHOW TABLES;
INSERT INTO students (name, course, mobile) values ('Emma Pike', "Math", 12341234)

