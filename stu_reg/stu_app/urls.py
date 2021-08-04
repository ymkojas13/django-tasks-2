from django.urls import path
from . import views

urlpatterns = [
    path('', views.stuindex2),
    path('index', views.stuindex),
]
