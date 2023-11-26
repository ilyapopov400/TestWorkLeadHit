FROM python:3.10

WORKDIR app/

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python homework/manage.py makemigrations
RUN python homework/manage.py migrate

#CMD ["python", "homework/manage.py", "runserver", "8000"]