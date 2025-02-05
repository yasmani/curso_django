from django.shortcuts import render, redirect
from .models import Contacto
from .forms import FormularioContacto

# Create your views here.

def contacto_lista(request):
    contacto = Contacto.objects.all()
    return render(request,'contacto/contacto_lista.html',{'contacto': contacto})


def contacto_agregar(request):
    if request.method == "POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('contacto_lista')
    else:
        formulario = FormularioContacto()
    return render(request, 'contacto/contacto_formulario.html',{'formulario': formulario})
    
    #realizar el CRUD