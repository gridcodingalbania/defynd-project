import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

#wsgi = imp.load_source('wsgi', 'manage.py')
#application = wsgi.application

wsgi = imp.load_source('wsgi', 'admin_panel/wsgi.py')
application = wsgi.application
