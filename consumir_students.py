import requests
import json
import time

BASE_URL = "http://localhost:8000/students"

# ----------------------------------------------------
# Función auxiliar para imprimir respuestas formateadas
# ----------------------------------------------------
def print_json_response(response):
    try:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except:
        print(response.text)

# ----------------------------------------------------
# GET - Obtener todos los estudiantes
# ----------------------------------------------------
def obtener_todos():
    print("\nLista completa de estudiantes:")
    response = requests.get(BASE_URL)
    print(f"Estado: {response.status_code}")
    print_json_response(response)
    time.sleep(1)

# ----------------------------------------------------
# GET - Obtener estudiante por ID
# ----------------------------------------------------
def obtener_por_id(student_id):
    print(f"\nConsultando estudiante con ID {student_id}...")
    response = requests.get(f"{BASE_URL}/{student_id}")
    print(f"Estado: {response.status_code}")
    print_json_response(response)
    time.sleep(1)

# ----------------------------------------------------
# POST - Crear estudiante con ID personalizado
# ----------------------------------------------------
def crear_estudiante(student_id, nombre, apellido, grado, grupo, fecha, parent_id):
    print(f"\nCreando estudiante con ID {student_id}...")
    data = {
        "student_id": student_id,
        "first_name": nombre,
        "last_name": apellido,
        "grade_level": grado,
        "group_name": grupo,
        "birth_date": fecha,
        "parent_id": parent_id,
        "status": "activo"
    }
    response = requests.post(BASE_URL, json=data)
    print(f"Estado: {response.status_code}")
    print_json_response(response)
    time.sleep(1)

# ----------------------------------------------------
# PUT - Modificar estudiante
# ----------------------------------------------------
def actualizar_estudiante(student_id, nuevo_grado, nuevo_grupo):
    print(f"\nActualizando estudiante con ID {student_id}...")
    data = {
        "grade_level": nuevo_grado,
        "group_name": nuevo_grupo,
        "status": "activo"
    }
    response = requests.put(f"{BASE_URL}/{student_id}", json=data)
    print(f"Estado: {response.status_code}")
    print_json_response(response)
    time.sleep(1)

# ----------------------------------------------------
# DELETE - Eliminar estudiante
# ----------------------------------------------------
def eliminar_estudiante(student_id):
    print(f"\nEliminando estudiante con ID {student_id}...")
    response = requests.delete(f"{BASE_URL}/{student_id}")
    print(f"Estado: {response.status_code}")
    print_json_response(response)
    time.sleep(1)

# ----------------------------------------------------
# SECUENCIA PRINCIPAL
# ----------------------------------------------------
if __name__ == "__main__":

    print("\n========== DEMOSTRACIÓN CRUD SIGE ==========")

    # 1. Mostrar lista inicial
    obtener_todos()

    # 2. Crear estudiantes con ID 3 y 4
    crear_estudiante(3, "Laura", "Martínez", "3°", "C", "2017-08-10", 1)
    crear_estudiante(4, "Diego", "Santos", "2°", "B", "2018-02-14", 2)

    # 3. Mostrar estudiante ID 3
    obtener_por_id(3)

    # 4. Mostrar estudiante ID 4
    obtener_por_id(4)

    # 5. Mostrar lista completa después de crearlos
    obtener_todos()

    # 6. Modificar estudiante ID 4
    actualizar_estudiante(4, "3°", "A")

    # 7. Mostrar lista completa tras la actualización
    obtener_todos()

    # 8. Eliminar estudiante ID 3
    eliminar_estudiante(3)

    # 9. Mostrar lista final
    obtener_todos()

    print("\nFin de la demostración CRUD SIGE\n")