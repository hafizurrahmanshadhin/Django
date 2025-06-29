# **Project Setup Instructions**

## **Follow these steps to set up a basic Python Django project**

## 1. Check Python Installation

**Verify that Python is correctly installed on your system:**

```shell
python --version
```

## 2. Create a Virtual Environment

**Create a new virtual environment in the current directory:**

```shell
python -m venv .venv
```

## 3. Activate the Environment

**Navigate into the virtual environment folder and activate it:**

```shell
.\.venv\Scripts\activate
```

**Then return to the main directory:**

```shell
cd ..
```

## 4. Install Django

**Use pip to install Django in the virtual environment:**

```shell
pip install django
```

## 5. Create a Django Project

**Start a new Django project named config in the current folder:**

```shell
django-admin startproject config .
```

## 6. Run the Development Server

**Confirm that the project is working:**

```shell
python manage.py runserver
```

## 7. Create a New Django App

**Create a Django app named myapp:**

```shell
python manage.py startapp myapp
```

---

## Project Re-Setup

```shell
pip freeze > requirements.txt
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

1. **pip freeze > requirements.txt**

   Saves currently installed packages (in the active environment) to requirements.txt.

2. **python -m venv .venv**

   Creates a new virtual environment named .venv.

3. **.venv\Scripts\activate**

   Activates the .venv environment.

4. **pip install -r requirements.txt**

   Installs all packages listed in requirements.txt inside the new environment.
