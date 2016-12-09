@echo off
virtualenv -p python.exe entorno
call entorno\Scripts\activate
pip install -r .\requirements.txt
python manage.py migrate