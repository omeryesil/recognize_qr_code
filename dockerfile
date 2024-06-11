FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libzbar0

COPY app/. /app

# RUN pip install --no-cache-dir Flask opencv-python pyzbar
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8800

CMD ["python", "api_app.py"]
