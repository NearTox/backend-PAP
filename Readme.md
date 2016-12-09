para correr por primera vez este bakend, es necesario utilizar los siguientes comandos:

>Windows:
```bash
.\install.bat
entorno\Scripts\activate
python manage.py migrate
python manage.py createsuperuser
```
>Linux:
```bash
bash .\install.sh
source entorno\bin\activate
python manage.py migrate
python manage.py createsuperuser
```
y para poder usarlo(normalmente  http://localhost:8000/):
```bash
python manage.py runserver
```