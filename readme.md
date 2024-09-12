# Car Management Web Application

## Project Overview
This is a web application for managing car information with the ability to leave comments. The application allows users to add, edit, and delete cars, view the list of all cars, and leave comments on them. It also features a REST API for interacting with the data.

### Key Features:
- Manage cars (add, edit, delete).
- Ability to leave comments on cars.
- User registration and authentication.
- Admin panel for managing cars and comments.
- REST API for working with car and comment data.

## Technology Stack:
- **Python 3.12**
- **Django 5.1.1**
- **Django REST Framework 3.15.2**
- **SQLite**

## Installation Guide

### 1. Prerequisites
Make sure you have the following installed on your system:
- Python 3.12
- Pip
- Git

### 2. Clone the repository
If you haven’t cloned the repository yet, run the following command to do so:

```bash
git clone <repository_url>
cd <repository_directory>
```

### 3. Install dependencies
Inside the project directory, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Database setup
Run the following commands to create and apply the database migrations:

```bash
python manage.py migrate
```

### 5. Create a superuser
To access the Django admin panel, create a superuser with administrative privileges:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up the superuser account.

### 6. Start the development server
Run the following command to start the Django development server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/.