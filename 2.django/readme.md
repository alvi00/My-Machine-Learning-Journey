
````markdown
# 🌀 Django Project Setup Guide


## 📦 1. Create a Virtual Environment

Start by creating a virtual environment to isolate your Python dependencies:

```bash
python -m venv alvi_venv
````

---

## 🔌 2. Activate the Virtual Environment

Activate the environment to start working inside it:

```bash
source alvi_venv/bin/activate
```

---

## 🧱 3. Install Django

Install Django into your virtual environment:

```bash
pip install django
```

---

## 🚀 4. Start the Django Project

Start your main Django project (replace `alvi_project` with your desired name):

```bash
django-admin startproject alvi_project .
```

> **Note**: The `.` at the end ensures the project is created in the current directory.

---

## 🧩 5. Create a Django App

Create your main app inside the project (replace `blog_app` with your app name):

```bash
python manage.py startapp blog_app
```

---

## 🛠️ 6. Register the App in `settings.py`

Open `alvi_project/settings.py` and add your app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'blog_app',
]
```

---

## 🧬 7. Make Migrations

After making changes in `models.py`, create migration files:

```bash
python manage.py makemigrations
```

---

## 📥 8. Apply Migrations

Apply all migrations to update the database schema:

```bash
python manage.py migrate
```

---

## 🔐 9. Create a Superuser (Admin Dashboard)

Set up your admin credentials to access the Django admin dashboard:

```bash
python manage.py createsuperuser
```

> Follow the prompts to set a username, email, and password.

---

## 🌐 10. Run the Development Server

Start your Django development server:

```bash
python manage.py runserver
```

Access the project at [http://127.0.0.1:8000](http://127.0.0.1:8000) and admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

---
