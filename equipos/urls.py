from django.urls import path

from equipos.views import lista_equipos, cargar_equipo

urlpatterns = [
    path("lista-equipos/", lista_equipos, name="lista_equipos"),
    path("carga-equipos", cargar_equipo, name="cargar_equipo")
     ]