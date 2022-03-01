"""litigation_management_software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path, url
from django.shortcuts import redirect
from clients import views as client
from django.conf import settings

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=True)),
    path('costStatements/', include('costStatements.urls')),  # it makes it public ?
    path('registration/', include('clients.urls')),
    path('litigation/', include('litigations.urls')),
    url(r'^attachments/', include('attachments.urls', namespace='attachments')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        client.activate, name='activate'),
    # path('media/documents/<slug:title>')
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

