# shop/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('statistics/', views.statistics_view, name='litigation-statistics')
]
