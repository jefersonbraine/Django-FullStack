from django.urls import path
from . import views

urlpatterns = [
    path('', views.convidados, name='convidados')
]