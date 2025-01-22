from django.http import HttpResponse
from django.shortcuts import render


#def hola_mundo(request):
    #return HttpResponse("Hola mundo..")
    
def index(request):
    return render(request,'index.html')