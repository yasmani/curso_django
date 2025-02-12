from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_vista , name='login'),
  #  path('register/', views.registro, name='registro'),
   # path('home/', views.home_vista, name='home'),
   # path('logout/',views.logout_vista, name='logout'),
]