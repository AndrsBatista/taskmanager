# Usa una imagen base oficial de Python
FROM python:3.12.3

WORKDIR /app

COPY . .
COPY start.sh /start.sh

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# El comando para ejecutar el servidor de desarrollo Django
RUN chmod +x /start.sh
CMD ["/start.sh"]


