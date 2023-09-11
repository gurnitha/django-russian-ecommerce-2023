# Django Russian Ecommerce

Mengulang latihan membuat aplikasi ecommerce berdasarkan tutorial Yuksel Celik di Youtube

## 1. SETUP

#### 1.1 Create and clone repository from Github

        modified:   README.md

## 2. PROJECT

#### 2.1 Create project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

## 3. DATABASE

#### 3.1 Instal Psycopg adaptor database PostgreSQL

        > python -m pip install psycopg2-binary

#### 3.2 Create db

        E:\_WORKSPACE\laragon\bin\postgresql\postgresql-15.3-4\bin
        λ psql
        psql (15.3)
        WARNING: Console code page (437) differs from Windows code page (1252)
                8-bit characters might not work correctly. See psql reference
                page "Notes for Windows users" for details.
        Type "help" for help.

        ING=# CREATE DATABASE django_russian_ecommerce_2023;
        CREATE DATABASE

#### 3.3 Connect db with the project

        modified:   README.md
        modified:   config/settings.py

#### 3.4 Instal django-environ

        > pip install django-environ
        (dj-russian-ecom) ING@AFTER65: pip list
        Package         Version
        --------------- -------
        asgiref         3.7.2
        Django          4.2
        django-environ  0.11.2
        pip             23.2.1
        psycopg2-binary 2.9.7
        setuptools      68.0.0
        sqlparse        0.4.4
        tzdata          2023.3
        wheel           0.41.2

#### 3.5 Create .env file

        new file:   .env.example
        modified:   .gitignore
        modified:   README.md

#### 3.6 Protecting sensitive file

        modified:   .env.example
        modified:   README.md
        modified:   config/settings.py

## 4. APP

#### 4.1 Membuat folder

        .
        ├── README.md
        ├── app
        │   └── home
        ├── config
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        └── manage.py

#### 4.2 Membuat home app

        modified:   README.md
        new file:   app/home/__init__.py
        new file:   app/home/admin.py
        new file:   app/home/apps.py
        new file:   app/home/migrations/__init__.py
        new file:   app/home/models.py
        new file:   app/home/tests.py
        new file:   app/home/views.py

        .
        ├── README.md
        ├── app
        │   └── home
        │       ├── __init__.py
        │       ├── admin.py
        │       ├── apps.py
        │       ├── migrations
        │       │   └── __init__.py
        │       ├── models.py
        │       ├── tests.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        └── manage.py

#### 4.3 Register home app to config/setting.spy

        modified:   README.md
        modified:   app/home/apps.py
        modified:   config/settings.py

## 5. TEMPLATES, VIEWS DAN URLS

#### 5.1 Hello World from HttpResponse

        modified:   README.md
        new file:   app/home/urls.py
        modified:   app/home/views.py
        modified:   config/urls.py

#### 5.2 Hello World from urls, views, templates

        modified:   README.md
        modified:   app/home/views.py
        modified:   config/settings.py
        new file:   templates/app/home/index.html

#### 5.3 Add html template to homepage

        modified:   README.md
        modified:   templates/app/home/index.html

## 6. STATIC FILES

#### 6.1 Create static folder

        modified:   README.md

#### 6.2 Add assets to static folder

        modified:   README.md
        new file:   static/css/bootstrap.min.css
        ...
        new file:   static/js/nouislider.min.js
        new file:   static/js/slick.min.js

#### 6.3 Configuring static files path

        modified:   README.md
        modified:   config/settings.py
        https://docs.djangoproject.com/en/4.2/howto/static-files/

#### 6.4 Load static files

        modified:   README.md
        modified:   templates/app/home/index.html

#### 6.4 Create base template and extends it to homepage

        modified:   README.md
        modified:   templates/app/home/index.html
        new file:   templates/base.html

#### 6.4 Template inheritance: header, navigation and footer

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/include/footer.html
        new file:   templates/include/header.html
        new file:   templates/include/navigation.html

#### 6.5 Template inheritance: homepage content

        modified:   README.md
        modified:   templates/app/home/index.html
        modified:   templates/base.html
