# Sistema Integral de Gestión Escolar (SIGE) - Backend

### Autor: Sebastián Ezequiel Coronado Rivera  
### Fecha: Octubre 2025  
### Video: https://youtu.be/Z9B-kgTzG7I?si=rs07bHvR6lecbruP
### Repo: 
---

## Descripción General

Este backend corresponde al módulo **students** del proyecto *Sistema Integral de Gestión Escolar (SIGE)*, diseñado para gestionar operaciones CRUD sobre estudiantes mediante una API REST desarrollada con **Flask** y conectada a **PostgreSQL**.  

El sistema implementa buenas prácticas de desarrollo backend, control de dependencias, estructura modular y soporte para ejecución en contenedores Docker.

---

## Estructura del Proyecto y Descripción de Archivos

| Archivo | Descripción |
|----------|--------------|
| **`SIGE_students.sql`** | Script SQL que crea la base de datos `SIGE`, las tablas `parents` y `students`, e inserta registros de ejemplo. |
| **`students_api.py`** | Código fuente del backend en Flask que expone las operaciones CRUD sobre la tabla `students`. |
| **`consumir_students.py`** | Script cliente en Python que consume los servicios web (GET, POST, PUT, DELETE) para probar la API sin usar Postman. |
| **`SIGE_Students_API.postman_collection.json`** | Colección de Postman lista para importar y probar los endpoints de la API de forma gráfica. |
| **`Dockerfile`** | Define la imagen Docker del backend Flask (instala dependencias, copia archivos y expone el puerto 8000). |
| **`docker-compose.yml`** | Orquesta dos servicios: `db` (PostgreSQL) y `backend` (Flask). Crea una red interna y configura la base de datos automáticamente. |
| **`README.md`** | Documento con instrucciones completas de instalación, ejecución, pruebas y uso de Docker. |

---

## Requisitos Previos

- **Python 3.10 o superior**
- **PostgreSQL instalado localmente**
- **Paquetes de Python necesarios:**
  ```bash
  pip install flask flask-cors psycopg2 requests
  ```

---

## Paso 1: Crear la Base de Datos Manualmente

1. Abre tu consola de PostgreSQL e importa el script SQL:
   ```sql
   \i 'ruta_al_archivo/SIGE_students.sql'
   ```
2. Verifica que existan las tablas:
   ```sql
   \dt
   ```

---

## Paso 2: Ejecutar el Backend Flask Localmente

1. Abre una terminal en la carpeta del proyecto:
   ```bash
   cd SIGE_Backend_Student
   ```
2. Ejecuta el servidor:
   ```bash
   python students_api.py
   ```
3. El backend se ejecutará en:  
   **http://localhost:8000**

---

## Paso 3: Probar con Postman

1. Importa el archivo `SIGE_Students_API.postman_collection.json` en Postman.  
2. Ejecuta los siguientes endpoints en orden:
   - **POST** `/students` → Crear un nuevo estudiante  
   - **GET** `/students` → Listar todos los estudiantes  
   - **GET** `/students/{id}` → Consultar estudiante por ID  
   - **PUT** `/students/{id}` → Actualizar información de un estudiante  
   - **DELETE** `/students/{id}` → Eliminar estudiante  

---

## Paso 4: Probar con el Cliente Python (`consumir_students.py`)

Este script permite consumir la API directamente desde Python mediante la librería `requests`.

1. Asegúrate de que el backend esté ejecutándose.
2. Corre el cliente:
   ```bash
   python consumir_students.py
   ```
3. El script realizará automáticamente las operaciones CRUD:
   - Crear un nuevo registro  
   - Consultar todos los registros  
   - Actualizar un registro  
   - Eliminar el registro creado  

---

## Paso 5: Ejecución con Docker (Opción Recomendada)

Como alternativa, el backend puede ejecutarse en contenedores Docker para garantizar portabilidad y reproducibilidad.

### Requisitos

- Tener **Docker Desktop** (Windows/macOS) o **Docker Engine + Docker Compose** (Linux).  
- Ubicarse en la carpeta raíz del proyecto.

---

### Instrucciones

1. Construir y levantar los contenedores:
   ```bash
   docker compose up --build
   ```
2. Esperar hasta que aparezca:
   ```
   * Running on http://0.0.0.0:8000
   ```
   Esto indica que la API Flask está activa dentro del contenedor.

3. Acceder a:
   ```
   http://localhost:8000/students
   ```

---

### Comandos útiles de Docker

| Comando | Descripción |
|----------|-------------|
| `docker compose ps` | Lista los contenedores activos |
| `docker compose down` | Detiene los servicios |
| `docker compose down -v` | Detiene y elimina los volúmenes (reinicio limpio) |
| `docker logs sige_backend` | Muestra los logs del contenedor Flask |
| `docker exec -it sige_db psql -U postgres -d SIGE` | Entra al contenedor de PostgreSQL |

---

### Notas Técnicas

- Puerto Flask: **8000**  
- Puerto PostgreSQL: **5432**  
- Usuario: **postgres**  
- Contraseña: **1234**  
- Base de datos: **SIGE**  
- El script `SIGE_students.sql` se ejecuta automáticamente al crear el contenedor de base de datos.

---

### Beneficios del uso de Docker

- Entorno reproducible y portable.  
- Aislamiento total de dependencias.  
- Ejecución consistente en cualquier equipo.  
- Cumplimiento con las buenas prácticas del objetivo **7.3** del curso.  

---

## Conclusión

Este backend cumple con los objetivos de la Actividad 8:  
**(7.2)** Integrar servicios web y APIs para exponer operaciones CRUD, y  
**(7.3)** Aplicar las mejores prácticas en la estructura y organización de proyectos de software.  

El proyecto puede ejecutarse localmente o en entornos Dockerizados, garantizando reproducibilidad, claridad estructural y una base sólida para futuras integraciones del sistema SIGE.

Desarrollado con fines académicos para la *Maestría en Inteligencia Artificial Aplicada – Tecnológico de Monterrey*.