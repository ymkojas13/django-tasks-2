from django.urls import path
from . import views

urlpatterns = [
    path('', views.empindex2, name='empindex'),
    path('index1', views.empindex, name='empindex1')
]
