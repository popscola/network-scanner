FROM python:3.9-slim

RUN apt-get update && apt-get install -y nmap

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
