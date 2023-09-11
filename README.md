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
