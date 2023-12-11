FROM python:3.10

SHELL ["/bin/bash", "-c"]

# set environment variabels
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update

WORKDIR app/

COPY .. .

EXPOSE 8000

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

#CMD ["python3", "homework/manage.py", "runserver", "8000"]

CMD ["gunicorn", "-b",  "127.0.0.1:8000", "homework.wsgi:application"]