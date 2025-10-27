# ----------------------------------------
# Dockerfile for SIGE Backend (Flask + PostgreSQL)
# ----------------------------------------

FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir flask flask-cors psycopg2-binary requests

EXPOSE 8000

CMD ["python", "students_api.py"]
