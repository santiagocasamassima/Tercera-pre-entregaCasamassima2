from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import equipos

# Create your views here.

def index(request):
    context = {
        "equipo" : "electrocardiografo"
    }
    http_response = render(
        request = request,
        template_name="index.html",
        context = context
    )
    return http_response

def lista_equipos(request):
    context = {
        "equipos" : [
            {"name" : "electrocardiografo", "ubicacion" : "cardiologia", "proveedor" : "agimed"},
            {"name" : "tomografo", "ubicacion" : "imagenes", "proveedor" : "philips"}
        ]
    }
    http_response = render(
        request = request,
        template_name="equipos/lista_equipos.html",
        context = context
    )
    return http_response

def cargar_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            ubicacion = data["ubicacion"]
        eq = equipos(nombre=nombre, descripcion=descripcion, ubicacion=ubicacion)
        eq.save()

        successful_url = reverse("lista_equipos")
        return redirect(successful_url)

    else:
        form = EquipoForm()
    http_response = render(
    request= request,
    template_name="equipos/carga_equipos.html",
    context={"form":form}
    )
    return http_response        