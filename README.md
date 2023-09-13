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

## 4. HOME APP

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

## 7. TEMPLATE INHERITANCE

#### 7.1 Create base template and extends it to homepage

        modified:   README.md
        modified:   templates/app/home/index.html
        new file:   templates/base.html

#### 7.2 Template inheritance: header, navigation and footer

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/include/footer.html
        new file:   templates/include/header.html
        new file:   templates/include/navigation.html

#### 7.3 Template inheritance: homepage content

        modified:   README.md
        modified:   templates/app/home/index.html
        modified:   templates/base.html

#### 7.4 Template inheritance: use block super for page title

        modified:   README.md
        modified:   templates/app/home/index.html
        modified:   templates/base.html

#### 7.5 House keeping: Modified README.md file

        modified:   README.md

## 8. PRODUCT APP

#### 8.1 Crete product folder: app/product

        modified:   README.md

#### 8.2 Crete product app

        modified:   README.md
        new file:   app/product/__init__.py
        new file:   app/product/admin.py
        new file:   app/product/apps.py
        new file:   app/product/migrations/__init__.py
        new file:   app/product/models.py
        new file:   app/product/tests.py
        new file:   app/product/views.py

#### 8.3 Register product app to config/settings.py

        modified:   README.md
        modified:   app/product/apps.py
        modified:   config/settings.py


## 9. MODEL

#### 9.1 Create Category model

        (dj-russian-ecom) λ pip install django-mptt

        (dj-russian-ecom) λ pip install pillow
        (dj-russian-ecom) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, 

        modified:   README.md
        modified:   app/product/models.py
        modified:   config/settings.py

#### 9.2 Create migration file and create table Category

        (dj-russian-ecom) λ python manage.py makemigrations
        (dj-russian-ecom) λ python manage.py migrate

        modified:   README.md
        new file:   app/product/migrations/0001_initial.py

#### 9.3 Admin - Activating Django Admin by creating superuser

        (dj-russian-ecom) λ python manage.py createsuperuser
        modified:   README.md

#### 9.4 Admin - Register Category model to product/admin.py

        modified:   README.md
        modified:   app/product/admin.py

#### 9.5 Admin - Menambahkan verbose_name_plural pada Category model

        modified:   README.md
        modified:   app/product/models.py

#### 9.6 Admin - Add a category in category tabel with error page not found

        modified:   README.md
        new file:   images/cat-women-clothing.png
        new file:   images/cat-women-clothing_VKsxfFG.png

        http://127.0.0.1:8000/images/cat-women-clothing_VKsxfFG.png
        Page not found (404)
        Request Method: GET
        Request URL:    http://127.0.0.1:8000/images/cat-women-clothing_VKsxfFG.png
        Using the URLconf defined in config.urls, Django tried these URL patterns, in this order:

        NEXT: Configure media path
