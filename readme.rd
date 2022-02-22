# Set up virtual environment

$ mkdir defynd-litigation-management-sw
$ cd defynd-litigation-management-sw
$ virtualenv env       || virtualenv -p python3.9 env  
$ env/Scripts/activate || source env/bin/activate

$ deactivate

$ pip install -r requirements.txt
-------
$ pip install django
$ pip install djangorestframework
$ python -m pip install django-cors-headers

# INSTALL DJANGO User Interface

$ pip install django-grappelli
or
$ pip install django-suit==0.2.25 (x)
pip install https://github.com/darklow/django-suit/tarball/v2

TODO: install changed django-suit (keep it apart in git)

or
$ pip install django-jet (install django version 1.0.8)

pip install django-nucleus

pip install django-material-admin
pip install django-material
pip install django-debug-toolbar

---
pip install django-excel
pip install django-funky-sheets
pip install django-gsheets

pip install django-import-export
pip install django-attachments

# Admin UI reorder apps
$ pip install django-modeladmin-reorder
$ pip install django-admin-menu
pip install django-slick-reporting
----

DJANGO ADMIN TOOLS
$ pip install django-admin-tools
$ pip install django-admin-tools-stats

DJANGO ADMIN CHARTS
$ pip install django-admin-charts

depedencies:
django-jsonfield
django-nvd3
django-bower

Reference:
https://pypi.org/project/django-admin-tools-stats/

https://ra-framework.readthedocs.io/_/downloads/en/latest/pdf/
https://github.com/ra-systems/django-ra-erp
https://ra-framework.readthedocs.io/en/latest/getting_started/integrating_into_django.html
https://github.com/farridav/django-jazzmin

https://github.com/ra-systems/django-slick-reporting

# ERP
$ pip install django-ra-erp
django-admin startapp sample_erp

# REPORTING
$ pip install django-reporting
$ pip install django-mr_reports
$ pip install django-model-report  !!!


# STATIC FILES
$ python manage.py collectstatic

# Create a new Django project
$ django-admin startproject litigation_management .  || admin_panel

# Create a new application in Django
$ django-admin startapp clients (moduli i klienteve, po i kontakteve?)
$ django-admin startapp lawyers (moduli i avokateve) ?
$ django-admin startapp litigations (moduli i ceshtjeve ligjore)
$ django-admin startapp costStatements (moduli ekonomik)
$ django-admin startapp contracts (moduli i kontratave)
$ django-admin startapp configurations (moduli i konfigurimeve)
$ django-admin startapp notifications (moduli i njoftimeve/emaileve)

# COMPUTED FIELDS ?
$ pip install django-computedfields

# Register applications at settings

$ python -m django --version 
-----------------------------------

# RUN MIGRATION
python manage.py migrate

Run 'python manage.py makemigrations' to make new migrations, and then re-run 'python manage.py migrate' to apply them.

$ python manage.py migrate --fake <appname>
(after moving a model in another app)

$ python manage.py migrate --fake-initial

python manage.py makemigrations --merge

# CREATE SUPERUSER
python manage.py createsuperuser

# RUN SERVER
$ python manage.py runserver


------------------------------
