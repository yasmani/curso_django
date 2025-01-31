from django.shortcuts import render
from .forms import RegistroUsuarioForms

# Create your views here.

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForms(request.POST)
        if form.is_valid():
            return render(request, 'usuarios/registro_exitoso.html')
    else:
        form = RegistroUsuarioForms()
        
    return render(request, 'usuarios/registro.html',{'form':form})    
