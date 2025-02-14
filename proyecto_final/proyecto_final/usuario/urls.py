from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_vista , name='login'),
   path('register/', views.registro_vista, name='registro_vista'),
   path('home/', views.home_vista, name='home'),
   # path('logout/',views.logout_vista, name='logout'),
]