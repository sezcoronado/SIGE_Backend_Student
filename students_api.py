from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Conexión con PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="sige",
    user="postgres",
    password="1234",
    port=5432
)
cursor = conn.cursor()

# CREATE
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    cursor.execute(
        '''INSERT INTO students (first_name, last_name, grade_level, group_name, birth_date, parent_id)
           VALUES (%s, %s, %s, %s, %s, %s) RETURNING student_id;''',
        (data['first_name'], data['last_name'], data['grade_level'], data['group_name'], data['birth_date'], data['parent_id'])
    )
    conn.commit()
    new_id = cursor.fetchone()[0]
    return jsonify({"message": "Estudiante agregado", "student_id": new_id}), 201

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
    cursor.execute(
        '''UPDATE students SET first_name=%s, last_name=%s, grade_level=%s, group_name=%s
           WHERE student_id=%s;''',
        (data['first_name'], data['last_name'], data['grade_level'], data['group_name'], id)
    )
    conn.commit()
    return jsonify({"message": "Estudiante actualizado"})

# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE student_id=%s;", (id,))
    conn.commit()
    return jsonify({"message": "Estudiante eliminado"})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
