#LoginForm
#RegisterForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

#formulario de registro
#class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #class Meta:
       # model = User
       # fields = ['nombre_usuario','email','password1','password2'] 

#formulario de login
class LoginForm(AuthenticationForm):
    nombre_usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput)
    