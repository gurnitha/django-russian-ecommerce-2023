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

#### 9.7 Admin - Configure media path

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

        NEXT: Re-add an image for category

#### 9.8 Admin - Re-add an image for category

        deleted:    images/cat-women-clothing_VKsxfFG.png
        renamed:    images/cat-women-clothing.png -> uploads/images/cat-women-clothing.png

        NEXT: Create Product model

#### 9.9 Admin - Add sub-categories and images for it

        new file:   uploads/images/sub-cat-women-clothing-2.png
        new file:   uploads/images/sub-cat-women-clothing.png

        NEXT: Create Product model

#### 9.10 Admin - Create Product model

        modified:   README.md
        modified:   app/product/models.py

        NEXT: Add Many-to-One relationship between Product and Category model

#### 9.11 Add Many-to-One relationship between Product and Category model

        modified:   README.md
        modified:   app/product/models.py

        NEXT: Create tabel Products by running migrations and migrate

#### 9.12 Admin - Create tabel Products by running migrations and migrate

        (dj-russian-ecom) λ python manage.py makemigrations
        (dj-russian-ecom) λ python manage.py migrate

        modified:   README.md
        new file:   app/product/migrations/0002_alter_category_options_product.py

        NEXT: Register Product model to product/admin.py

#### 9.13 Admin - Register Product model to product/admin.py

        modified:   README.md
        modified:   app/product/admin.py

        NEXT: Add items to products table

#### 9.14 Admin - Add items to products table

        modified:   README.md
        modified:   app/product/admin.py
        new file:   uploads/images/product-dresses-1.png
        new file:   uploads/images/product-dresses-2.png
        new file:   uploads/images/product-skirt-1.png
        new file:   uploads/images/product-skirt-2.png

        NEXT: Modify Categories and Products display in admin dashboard

#### 9.15 Admin - Modify Categories and Products display in admin dashboard

        modified:   README.md
        modified:   app/product/admin.py

        NEXT: Showing category image thumbnails in Admin dashboard

#### 9.16 Admin - Showing category image thumbnails in Admin dashboard

        modified:   README.md
        modified:   app/product/admin.py
        modified:   app/product/models.py

        NEXT: Showing product image thumbnails in Admin dashboard

#### 9.17 Admin - Showing product image thumbnails in Admin dashboard

        modified:   README.md
        modified:   app/product/admin.py
        modified:   app/product/models.py

        NEXT: Create Image model for image gallery

#### 9.18 Admin - Create Image model for image gallery

        (dj-russian-ecom) λ python manage.py makemigrations
        (dj-russian-ecom) λ python manage.py migrate

        modified:   README.md
        modified:   app/product/admin.py << --- register Image model
        new file:   app/product/migrations/0003_images.py << -- create table
        modified:   app/product/models.py << --- create Image model

        NEXT: Use TabularInline for image galerry

#### 9.19 Admin - Use TabularInline/imageinline to add more images for a product

        modified:   README.md
        modified:   app/product/admin.py
        new file:   uploads/images/skirt-gal-blue.png
        new file:   uploads/images/skirt-gal-blue_kN51cn0.png
        new file:   uploads/images/skirt-gal-dark.png
        new file:   uploads/images/skirt-gal-green.png
        new file:   uploads/images/skirt-gal-phink.png

        NEXT: Install Django CKEditor

#### 9.20 Admin - Setup Django CKEditor

        (dj-russian-ecom) λ pip install django-ckeditor

        modified:   README.md
        modified:   app/product/models.py
        modified:   config/settings.py
        modified:   config/urls.py

        NEXT: Make slug pre-populated

#### 9.21 Admin - Make slug pre-populated

        modified:   README.md
        modified:   app/product/admin.py
        modified:   app/product/models.py

        NEXT: Cleaning old data and re-iput new data

#### 9.22 Admin - Cleaning old data and re-iput new data

        (dj-russian-ecom) λ python manage.py makemigrations
        (dj-russian-ecom) λ python manage.py migrate
        (dj-russian-ecom) λ python manage.py createsuperuser

        modified:   README.md
        new file:   app/product/migrations/0004_alter_images_options_alter_product_detail.py
        ...
        deleted:    uploads/images/sub-cat-women-clothing.png

        NEXT: Create project's settings


## 10. PROJECT'S SETTINGS 

#### 10.1 Create Setting model for project's settings

        modified:   README.md
        modified:   app/home/models.py

#### 10.2 Create table Setting by running migration

        (dj-russian-ecom) λ python manage.py makemigrations
        (dj-russian-ecom) λ python manage.py migrate

        modified:   README.md
        new file:   app/home/migrations/0001_initial.py

        NEXT: Register Setting model to home/admin.py

#### 10.3 Register Setting model to home/admin.py

        modified:   README.md
        modified:   app/home/admin.py

        NEXT: Add block tags to head

#### 10.4 Add block tags to meta keywords and description in head

        modified:   README.md
        modified:   templates/base.html

        NEXT: Setup static title for page title, keywords, and description

#### 10.5 Setup static title for page title, keywords, and description

        <!-- templates/app/home/index.html -->
        {% block title %} My static page title {% endblock %} 
        {% block keywords %} My static keywords {% endblock %} 
        {% block description %} My static description {% endblock %} 

        <!-- Results -->
        <!-- app/home/templates/home/index.html -->
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
            <title>
               My static page title  | eShop 
            </title>
            <meta name="keywords" content=" My static keywords " />
            <meta name="description" content=" My static description " />

        modified:   README.md
        modified:   templates/app/home/index.html

        NEXT: Input data to Setting table