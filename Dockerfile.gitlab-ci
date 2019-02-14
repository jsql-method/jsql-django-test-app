FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
RUN rm -rfv Dockerfile* .gitlab-ci.yml LICENSE README.md *.sh run-python.txt

RUN pip install --upgrade pip && \
    pip install virtualenv

RUN chmod +x ./venv/Scripts/activate ./mrdj/manage.py
RUN ./venv/Scripts/activate
RUN pip install -r requirements.txt
CMD ./mrdj/manage.py runserver 0.0.0.0:8000


#Pytanie odnośnie tej komendy
# python manage.py migrate'
