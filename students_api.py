from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
import time
from psycopg2 import OperationalError

app = Flask(__name__)
CORS(app)

# Function to wait until the database is ready
def wait_for_db(host, dbname, user, password, retries=10, delay=3):
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host=host,
                database=dbname,
                user=user,
                password=password
            )
            conn.close()
            print(f"Database connection successful on attempt {attempt + 1}")
            return True
        except OperationalError as e:
            print(f"Waiting for database... attempt {attempt + 1}/{retries}")
            time.sleep(delay)
    print("Could not connect to the database after several attempts.")
    return False

# --- Wait for DB before proceeding ---
DB_HOST = "db"
DB_NAME = "sige"
DB_USER = "postgres"
DB_PASS = "1234"

wait_for_db(DB_HOST, DB_NAME, DB_USER, DB_PASS)

# Conexión con PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "db"),
    database=os.getenv("DB_NAME", "SIGE"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "1234"),
    port=os.getenv("DB_PORT", 5432)
)
#conn = psycopg2.connect(
#    host="localhost",
#    database="sige",
#    user="postgres",
#    password="1234",
#    port=5432
#)
cursor = conn.cursor()

# CREATE
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    cursor = conn.cursor()

    # Check if student_id is provided by the user
    student_id = data.get("student_id")

    # If student_id provided, verify it doesn't already exist
    if student_id is not None:
        cursor.execute("SELECT student_id FROM students WHERE student_id = %s;", (student_id,))
        if cursor.fetchone():
            return jsonify({"error": f"Student ID {student_id} already exists."}), 400

        # Insert using the provided ID
        cursor.execute("""
            INSERT INTO students (student_id, first_name, last_name, grade_level, group_name, birth_date, parent_id, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING student_id;
        """, (
            student_id,
            data["first_name"],
            data["last_name"],
            data["grade_level"],
            data["group_name"],
            data["birth_date"],
            data["parent_id"],
            data["status"]
        ))
    else:
        # No ID provided → use default SERIAL increment
        cursor.execute("""
            INSERT INTO students (first_name, last_name, grade_level, group_name, birth_date, parent_id, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING student_id;
        """, (
            data["first_name"],
            data["last_name"],
            data["grade_level"],
            data["group_name"],
            data["birth_date"],
            data["parent_id"],
            data["status"]
        ))

    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return jsonify({"message": "Student added successfully", "student_id": new_id}), 201

# READ ALL
@app.route('/students', methods=['GET'])
def get_students():
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    return jsonify(students)

# READ ONE
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    cursor.execute("SELECT * FROM students WHERE student_id = %s;", (id,))
    student = cursor.fetchone()
    return jsonify(student) if student else ("No encontrado", 404)

# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    cursor = conn.cursor()

    # Obtener el estudiante actual
    cursor.execute("SELECT first_name, last_name, grade_level, group_name, status FROM students WHERE student_id = %s;", (id,))
    current = cursor.fetchone()
    if not current:
        return jsonify({"error": "Estudiante no encontrado"}), 404

    # Mantener los valores existentes si no se envían nuevos
    first_name = data.get('first_name', current[0])
    last_name = data.get('last_name', current[1])
    grade_level = data.get('grade_level', current[2])
    group_name = data.get('group_name', current[3])
    status = data.get('status', current[4])

    cursor.execute('''
        UPDATE students 
        SET first_name=%s, last_name=%s, grade_level=%s, group_name=%s, status=%s
        WHERE student_id=%s;
    ''', (first_name, last_name, grade_level, group_name, status, id))

    conn.commit()
    cursor.close()
    return jsonify({"message": f"Estudiante {id} actualizado correctamente"})

# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE student_id=%s;", (id,))
    conn.commit()
    return jsonify({"message": "Estudiante eliminado"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
