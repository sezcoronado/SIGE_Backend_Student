# Sistema Integral de Gestión Escolar (SIGE) - Backend

### Autor: Sebastián Ezequiel Coronado Rivera  
### Fecha: Octubre 2025  

---

## Descripción General

Este backend corresponde al módulo **students** del proyecto *Sistema Integral de Gestión Escolar (SIGE)*, diseñado para gestionar operaciones CRUD sobre estudiantes mediante una API REST desarrollada con **Flask** y conectada a **PostgreSQL**.

El paquete incluye:
1. `SIGE_students.sql` → Script SQL para crear la base de datos, tablas y datos de ejemplo.
2. `students_api.py` → Código fuente de la API Flask.
3. `SIGE_Students_API.postman_collection.json` → Colección Postman para probar los endpoints.
4. `README.md` → Instrucciones de instalación y uso.

---

## Requisitos Previos

- Python 3.10 o superior  
- PostgreSQL instalado localmente  
- Paquetes de Python:
  ```bash
  pip install flask flask-cors psycopg2 requests
  ```

---

## Paso 1: Crear la base de datos

1. Abre tu consola de PostgreSQL e importa el script SQL:
   ```sql
   \i 'ruta_al_archivo/SIGE_students.sql'
   ```
2. Verifica que existan las tablas `parents` y `students`:
   ```sql
   \dt
   ```

---

## Paso 2: Ejecutar el backend Flask

1. Abre una terminal en la carpeta del proyecto.  
2. Ejecuta el servidor con:
   ```bash
   python students_api.py
   ```
3. El backend se ejecutará en:  
   **http://localhost:8000**

---

## Paso 3: Probar con Postman

1. Importa el archivo `SIGE_Students_API.postman_collection.json` en Postman.  
2. Ejecuta los siguientes endpoints en orden:
   - **POST** `/students` → Crear estudiante
   - **GET** `/students` → Listar todos
   - **GET** `/students/{id}` → Consultar por ID
   - **PUT** `/students/{id}` → Actualizar estudiante
   - **DELETE** `/students/{id}` → Eliminar estudiante

---

## Notas Técnicas

- Puerto por defecto: **8000**
- Usuario de BD: **postgres**
- Contraseña: **1234**
- Host: **localhost**
- Base de datos: **SIGE**

---

## 🏁 Conclusión

Este avance cumple con los objetivos de la Actividad 8:  
**(7.2)** Integrar servicios web y APIs para exponer operaciones CRUD, y  
**(7.3)** aplicar buenas prácticas en la estructura de proyectos de software.

Desarrollado con fines académicos para la Maestría en Inteligencia Artificial Aplicada - Tecnológico de Monterrey.
