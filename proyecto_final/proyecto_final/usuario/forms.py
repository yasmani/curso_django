from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserCreationForm
from .models import Usuario

#formulario de registro
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True,widget=forms.TextInput(attrs={
        'type':'date'
    }))
    class Meta:
       model = Usuario
       fields = ['username','email','password1','password2','fecha_nacimiento'] 

#formulario de login
class LoginForm(AuthenticationForm):
    nombre_usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput)
    