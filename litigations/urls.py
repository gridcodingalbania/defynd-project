from django.urls import path
from . import views

urlpatterns = [
    path('<slug:lang>', views.litigation_view, name='litigation_view'),
]
