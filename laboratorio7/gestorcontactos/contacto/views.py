from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contacto
from .forms import FormularioContacto

# Create your views here.

def sispa_index(request):
    return render(request,'contacto/sispa.html')

def contacto_lista(request):
    contacto = Contacto.objects.all()
    messages.success(request,'Lista de Contactos..')
    return render(request,'contacto/contacto_lista.html',{'contacto': contacto})


def contacto_agregar(request):
    if request.method == "POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Contacto Agregado..')
            return redirect('contacto_lista')
    else:
        formulario = FormularioContacto()
    return render(request, 'contacto/contacto_formulario.html',{'formulario': formulario})
    
    
    #realizar el CRUD

def contacto_editar(request, pk):
    contacto=get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        formulario = FormularioContacto(request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Contacto Editado..')
            return redirect('contacto_lista')
    else:
        formulario=FormularioContacto(instance=contacto)
    return render(request, 'contacto/contacto_formulario.html',{'formulario': formulario})
    
    
def elimina_contacto(request, pk):
    contacto=get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        contacto.delete()
        messages.success(request,'Contacto Eliminado..')
        return redirect('contacto_lista')
    return render(request, 'contacto/contacto_confirmar_eliminar.html',{'contacto': contacto})
     