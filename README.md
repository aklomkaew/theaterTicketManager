# theaterTicketManager

* Install django. Good tutorial: https://tutorial.djangogirls.org/en/django_installation/. Also good overview: https://tutorial.djangogirls.org/en/installation/
* Install postgresql. Good tutorial: https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/
* Replace the database section of the settings.py file with:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ttm',
        'USER': 'ttm',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
* In the mysite folder, run: python manage.py createsuperuser to create an administrator user.
* Data models are defined in models.py. Read for more details: https://docs.djangoproject.com/en/2.1/topics/db/
* If you make any changes to the data model, you must run:
    python manage.py makemigrations
    python manage.py migrate
* To start the server, run:
    python manage.py runserver
* To browse to the server, go to: http://127.0.0.1:8000
* To browse to the admin page, go to: http://127.0.0.1:8000/admin/
