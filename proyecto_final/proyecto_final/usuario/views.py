from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from .forms import RegisterForm,LoginForm

# Create your views here.
def login_vista(request):
    if request.method == 'POST':
        formulario = LoginForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('nombre_usuario')
            contrasena = formulario.cleaned_data.get('contrasenaa') 
            user = authenticate(nombre_usuario=nombre_usuario, contrasena=contrasena)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        formulario = LoginForm()
    return render(request, 'usuario/login.html',{'formulario': formulario})
    
    
#def registro(request):
    
    
#def home_vista(request):
    
    
    
#def logout_vista(request):