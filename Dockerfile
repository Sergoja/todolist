FROM python:3.11.2

WORKDIR /app/todolist-api
COPY requirements.txt /app/todolist-api
RUN pip install -r /app/todolist-api/requirements.txt
COPY  . .
CMD python manage.py runserver 0.0.0.0:8000