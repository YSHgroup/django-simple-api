# django-simple-api

## Collection of the commands for beginer
```
pip install django
django-admin startproject [project name]
cd [project name]
python manage.py startapp [app name]
python manage.py makemigrations
python manage.py migrate
```

## pip-tools
```
    pip install pip-tools
    pip freeze
    touch requirements.in
    pip-compile --output-file=requirements.txt requirements.in
    pip install -r requirements.txt
```

## Setting up a project on another machine
From here, you shouldn’t install packages using pip install <package-name>

Every time you want to add a package, you need to go through the following steps:

- Add the package name to requirements.in
- Compile the requirements using `pip-compile --output-file=requirements.txt requirements.in`
- Install the requirements using `pip install -r requirements.txt`
- Commit both `requirements.txt` and `requirements.in` to your remote repository.
- By committing `requirements.txt` as well as `requirements.in`, you won’t have to recompile the requirements when setting up your project on another machine.

## Content
This project consist two sub projects:
- crud_app (Backend and Frontend by built in API module)
- server (Backend by using the DRF)

### Server
 This project is for using the Django Rest Framework(DRF).

- [movie](https://medium.com/@learncodeguide/creating-a-crud-api-with-django-rest-framework-and-postgresql-3ead7ffb140f)
 