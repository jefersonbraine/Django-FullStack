from django.urls import path
from . import views

urlpatterns = [
    path('', views.convidados, name='convidados'),
    path('responder_presenca/', views.responder_presenca, name='responder_presenca'),
]