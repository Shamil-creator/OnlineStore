создаем проект
django-admin startproject common 

создаем приложение
python manage.py startapp store

подключаем базу и создаем вспомогательные таблицы
python manage.py migrate 

запускаем приложение
python manage.py runserver

изменения которые мы делаем в базе
python manage.py makemigrations
python manage.py migrate

создаем админа 
python manage.py createsuperuser