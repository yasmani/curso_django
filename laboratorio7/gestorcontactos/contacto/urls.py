from django.urls import path
from . import views

urlpatterns = [
    path('', views.sispa_index, name='sispa_index'),
    path('contacto/', views.contacto_lista, name='contacto_lista'),
    path('agregar/', views.contacto_agregar, name='contacto_agregar'),
    path('eliminar/', views.elimina_contacto, name='elimina_contacto'),
     path('editar/<int:pk>', views.contacto_editar, name='contacto_editar'),
]