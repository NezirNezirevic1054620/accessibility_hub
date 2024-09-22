FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /accessibility_hub

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY accessibility_hub .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]