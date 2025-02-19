from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, LoginForm
from .models import Usuario

# Create your views here.
def login_vista(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
           usuario = formulario.get_user()
           login(request,usuario)
           return redirect('home')
    else:
        formulario = AuthenticationForm()
        #formulario = LoginForm()
    return render(request, 'usuarios/login.html',{'formulario': formulario})
    
    
def registro_vista(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data.get('username')
            passwoord = formulario.cleaned_data.get('passwoord1')
            usuario = authenticate(username=username, passwoord=passwoord)
            login(request,usuario)
            return redirect('login')
    else:
        formulario = RegistroForm()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})
    
def home_vista(request):
    usuarios = Usuario.objects.all()
    return render(request,'usuarios/home.html',{'usuarios': usuarios})
    
    
    
