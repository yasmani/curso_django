from django.shortcuts import render

# Create your views here.

def lista_tareas(request):
    tareas=[
        {'nombre':'04.00 pm Sumergirme en mi propia miseria'},
        {'nombre':'04.30 pm Contemplar el abismo'},
        {'nombre':'05.00 pm Solucionar la hambruna mundial sin decírselo a nadie'},
        {'nombre':'05.30 pm Danza y ejercicio '},
        {'nombre':'06.30 pm Cena conmigo. Esa no la cancelare!!'},
        {'nombre':'07.00 pm Luchar con el odio que me tengo'},
        ]
    return render(request,'tareas/lista_tareas.html',{'tareas':tareas})
    