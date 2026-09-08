FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY mensagens.py .

CMD ["python", "app.py"]
