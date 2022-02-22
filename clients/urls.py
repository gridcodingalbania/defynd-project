from django.urls import path
from . import views

urlpatterns = [
    path('<slug:lang>', views.register, name='register'),
]
