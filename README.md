# Django Restaurant

A simple restaurant management and ordering web application built with Django.  
This project is deployed on Render.com and designed for easy local development and deployment.

## Features

- Menu browsing
- Order placement
- Basic restaurant management features

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/MarkoAtanasovski/django-restaurant.git
cd django-restaurant


Create and activate a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

Configuration

Make sure ALLOWED_HOSTS in django_restaurant/settings.py includes your local hosts:

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

If you use environment variables, set them accordingly or create a .env file.

Running the Project Locally

Apply migrations:

python manage.py migrate

Create a superuser (optional, for admin access):

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Visit http://localhost:8000 in your browser.







