# Golf Score Keeper

DETAILS COMING SOON.

Tech Stack:

Django
Postgresql
htmx to give some features a SPA feel
NiceAdmin theme by BootstrapMade

Running the code:

You'll need a .env file in the root that contains the following:

```
SECRET_KEY=
DB_HOST=
DB_NAME=
DB_PASSWORD=
DB_PORT=
DB_USER=
DEBUG=1

ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 
EMAIL_PORT=

EMAIL_USERNAME=
EMAIL_PASSWORD=
FROM_EMAIL=
APP_NAME=

APP_URL=127.0.0.1:8000

DEFAULT_EMAIL=
```

After creating your virtual environment (optional but recommended), install the dependencies.

```
pip install -r requirements.txt
```

Make migrations and apply to the DB.

```
py manage.py makemigrations
py manage.py migrate
```

Finally, run the server.

```
py manage.py runserver
```