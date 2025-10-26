import requests
import json

BASE_URL = "http://localhost:8000/students"

# ----------------------------------------------------
# GET - Obtener todos los estudiantes
# ----------------------------------------------------
def get_all_students():
    print("\nObteniendo todos los estudiantes...")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("Estudiantes obtenidos con éxito:\n")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error de conexión: {e}")


# ----------------------------------------------------
# POST - Crear un nuevo estudiante
# ----------------------------------------------------
def create_student():
    print("\nCreando nuevo estudiante...")
    data = {
        "first_name": "Laura",
        "last_name": "Martínez",
        "grade_level": "3°",
        "group_name": "C",
        "birth_date": "2017-08-10",
        "parent_id": 1
    }
    try:
        response = requests.post(BASE_URL, json=data)
        print(f"Respuesta ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error: {e}")


# ----------------------------------------------------
# PUT - Actualizar estudiante existente
# ----------------------------------------------------
def update_student(student_id):
    print(f"\nActualizando estudiante con ID {student_id}...")
    data = {
        "first_name": "Laura Elena",
        "last_name": "Martínez",
        "grade_level": "3°",
        "group_name": "B"
    }
    try:
        response = requests.put(f"{BASE_URL}/{student_id}", json=data)
        print(f"Respuesta ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error: {e}")


# ----------------------------------------------------
# DELETE - Eliminar estudiante
# ----------------------------------------------------
def delete_student(student_id):
    print(f"\nEliminando estudiante con ID {student_id}...")
    try:
        response = requests.delete(f"{BASE_URL}/{student_id}")
        print(f"Respuesta ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error: {e}")


# ----------------------------------------------------
# Programa principal
# ----------------------------------------------------
if __name__ == "__main__":
    # 1. Crear nuevo estudiante
    create_student()

    # 2. Ver todos los registros
    get_all_students()

    # 3. Actualizar uno existente (por ejemplo, el ID 3)
    update_student(3)

    # 4. Eliminar estudiante (ID 3)
    delete_student(3)