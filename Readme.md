# Tech Mahindra Task 1 - CRUD Form In Django Framework
![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)

## To get started
- Clone the repository
- Download Docker Desktop for windows
- Start docker container
    - To create the instance in the current project directory:
    ```
    docker-compose build
    ```
    - Now we run our instance in one terminal and switch to a new terminal for further queries:
    ``` 
    docker-compose up 
    ```
    - Go to localhost:80 for php-my-admin 
    ```
    web-server: db
    username: root
    password: root
    ```
    - Set the config in settings.py
    ```
    DATABASES ={
        'default':{
            'ENGINE':'django.db.backends.mysql',
            'NAME':'<database_name>',
            'USER':'root',
            'PASSWORD':'root',
            'HOST':'db',
            'PORT':'3306',
        }
    } 
    ```
    - Migrate the changes to mysql database
    ```
    docker-compose run --rm web python manage.py migrate
    ```
    - To run bash terminal to execute 'python manage.py' commands
    ```
    docker-compose run --rm web bash
    ```
    - Install the dependencies
    ```
    docker-compose run --rm web pip install -r requirements.txt
    ```
    - Starting the development server on localhost:<any-ip>
    ```
    docker-compose run --rm web python manage.py runserver 127.0.0.1:<any-ip>
    ```

# Some Included Functionalities
- MySQL Database Setup
- Simple CRUD Form 
- Django Admin Customisation
- Database Schema, Models and Migrations
- Use of docker to run on any operating system

## Some Important commands
### Virtual Environment Setup
```
Pip install virtualenv
python -m venv env
.\env\Scripts\activate
```

### Install Django & Start the project
```
Python –m Pip install django
django-admin startproject carzone
python manage.py startapp pages
python manage.py runserver
```

### To Add Static Files From STATIC_FILES_DIR to STATIC_ROOT
```
python manage.py collectstatic
For .env
pip install python-decouple
```

### For postgres sql
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### For Production
```
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth Permission --indent 4 > project_dump.json
pip install gunicorn psycopg2-binary
pip install dj-database-url
pip install whitenoise
pip freeze > requirements.txt
```

### For Heroku
```
git add .
git commit –m “production”
git push heroku master
heroku open
heroku run python manage.py loaddata project_dump.json
Run a bash inside heroku
heroku login
heroku run bash -a APPNAME
$ cd app
```

### Website Themes
```
http://www.themelock.com/
https://www.themes24x7.com/xstore-v7-0-responsive-multi-purpose-woocommerce-wordpress-theme/
```

