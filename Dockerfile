FROM python:3
WORKDIR /Cuatro_en_Linea_Docker

COPY . .
CMD ["python3","test.py"]