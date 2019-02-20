CALL pip install virtualenv
CALL ./venv/Scripts/activate
CALL pip install -r requirements.txt
CALL cd mrdj
CALL manage.py runserver --settings=settings.dev