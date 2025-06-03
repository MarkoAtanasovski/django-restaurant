FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . /app/

# Make sure STATIC_ROOT is set in settings.py before running this
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "Restaurant_Project.wsgi:application", "--bind", "0.0.0.0:8000"]
