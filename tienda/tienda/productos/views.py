from django.shortcuts import render

# Create your views here.

def lista_productos(request):
    productos=[
            {'nombre':'Camisa','precio':20,'oferta':True},
            {'nombre':'Pantalon','precio':80,'oferta':True},
            {'nombre':'Polera','precio': 40,'oferta':False},
            {'nombre':'Zapatos','precio':120,'oferta':True},
            {'nombre':'Vestidos','precio':60,'oferta':False},      
    ]
    return render(request,'productos/lista_productos.html',{'productos': productos})