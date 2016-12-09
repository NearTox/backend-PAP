@echo off
virtualenv -p python.exe entorno
call entorno\Scripts\activate
pip install -r .\requirements.txt --no-cache-dir
python manage.py migrate