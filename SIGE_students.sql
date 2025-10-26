-- ===========================================
-- Script: SIGE_students.sql
-- Proyecto: Sistema Integral de Gestión Escolar (SIGE)
-- Descripción: Creación de la base de datos y tabla students
-- Autor: Sebastián Ezequiel Coronado Rivera
-- Fecha: Octubre 2025
-- ===========================================

CREATE DATABASE sige;
\c sige;

CREATE TABLE parents (
    parent_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    grade_level VARCHAR(20) NOT NULL,
    group_name VARCHAR(20),
    birth_date DATE,
    parent_id INT REFERENCES parents(parent_id) ON DELETE SET NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_students_parent ON students(parent_id);
CREATE INDEX idx_students_grade ON students(grade_level);

INSERT INTO parents (first_name, last_name, email, phone)
VALUES ('Ana', 'Gómez', 'ana.gomez@example.com', '555-1234'),
       ('Luis', 'Ramírez', 'luis.ramirez@example.com', '555-5678');

INSERT INTO students (first_name, last_name, grade_level, group_name, birth_date, parent_id)
VALUES ('Carlos', 'Ramírez', '3°', 'B', '2017-04-15', 2),
       ('Valeria', 'Gómez', '2°', 'A', '2018-03-22', 1);

SELECT * FROM parents;
SELECT * FROM students;
