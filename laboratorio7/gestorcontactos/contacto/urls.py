from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_lista, name='contacto_lista'),
    path('agregar/', views.contacto_agregar, name='contacto_agregar'),
]