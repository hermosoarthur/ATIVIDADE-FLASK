# Usa imagem base do Python
FROM python:3.10


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5002


CMD ["python", "app.py"]
