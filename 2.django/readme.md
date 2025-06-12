1. At first what i have to do is  this - python -m venv alvi_venv
to create a ventual environment

2. Then what I had to do is source alvi_venv/bin/activate
to active the venv

3. then i had to install django by this pip install django

4. then to start a project i had to write this - django-admin startproject alvi_project .

5. then to start our main project i had to write python manage.py startapp blog_app

6. Had to add blog_app in settings.py

7. if i make any changes in the app's model.py and it should migrate to the whole projet that's why I had to do python manage.py makemigrations

8. then to migrate i had to write python manage.py migrate
 
9. to create a dashboard i had to write python manage.py createsuperuser

10. to run the server i has to write python manage.py runserver