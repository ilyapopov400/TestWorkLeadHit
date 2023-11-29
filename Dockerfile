FROM python:3.10

SHELL ["/bin/bash", "-c"]

# set environment variabels
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update

WORKDIR app/

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

RUN python homework/manage.py makemigrations
RUN python homework/manage.py migrate

CMD ["python", "homework/manage.py", "runserver", "8000"]