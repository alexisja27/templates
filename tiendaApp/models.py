from django.db import models

# Create your models here.
productos = {
    101: ["teclado", "hp", "xr:25", 12000, "teclado.jpg"],
    102: ["mouse", "microsoft", "LDP-101", 17500, "mouse.jpg"],
    103: ["monitor", "lg", "xc54", 185000, "monitor.jpg"],
    104: ["monitor", "samsung", "aw780", 205000, "monitor2.jpg"],
    105: ["notebook", "sony", "vr980", 850000, "notebook.jpg"],
    106: ["notebook", "hp", "lo852", 750000, "notebook2.jpg"],
}

vendedores = [
    {"nombre": "juan", "apellido": "ramirez contreras"},
    {"nombre": "marcos", "apellido": "veas araya"},
    {"nombre": "emilia", "apellido": "juarez farias"},
    {"nombre": "rosa", "apellido": "narvaes solano"},
    {"nombre": "pedro", "apellido": "salas novoa"},
]
