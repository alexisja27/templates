from django.shortcuts import render
from tiendaApp import models as datos


# Create your views here.
def inicio(request):
    return render(request, "tiendaApp/inicio.html")


def personal(request):
    data = {
        "nombre": "carlos",
        "paterno": "Palacios",
        "materno": "nuñez",
        "edad": 24,
        "correo": "carlospalacio@gmail.com",
        "cargo": "futbolista",
    }
    return render(request, "tiendaApp/usuarios.html", data)


def catalogo(request):
    data = {
        "productos": datos.productos,
        "vendedores": datos.vendedores,
    }
    return render(request, "tiendaApp/catalogo.html", data)
