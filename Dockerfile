# Usa una imagen base oficial de Python
FROM python:3.12.3

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . .
COPY requirements.txt .
# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto para que el contenedor sea accesible
EXPOSE 8000

# El comando para ejecutar el servidor de desarrollo Django
CMD ["python", "task_manager/manage.py", "runserver", "0.0.0.0:8000"]
