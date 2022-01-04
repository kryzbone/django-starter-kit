# django-starter-kit

It comes packaged with `django_restframework`, `def_yasg` for api documentation, 
`custom user model`, `pre-commit` package, `djoser` for authentication, 
`django-environ` for .env. The default database setup is `postgres`.

### Set up enviroment and run

1. Set up python and virtual enviroment
```
$ python -m venv env
linux os 
$ source env/bin/activate 
win os 
$ env/Scripts/activate
$ pip install -r requirements.txt
```

2. Create `.env` file in the root dir and add `DATABASE_URL=<your db url>`

3. Run the initial migrations,build the database, create user and run project

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
