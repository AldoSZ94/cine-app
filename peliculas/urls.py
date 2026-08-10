from django.urls import path
from . import views

app_name = "peliculas"

urlpatterns = [
    path("", views.lista_peliculas, name="lista_peliculas"),
    path(
        "detalle_pelicula/<int:pk>/",
        views.detalle_pelicula,
        name="detalle_pelicula",
    ),
    path("editar_pelicula/<int:pk>/", views.editar_pelicula, name="editar_pelicula"),
    path(
        "eliminar_pelicula/<int:pk>", views.eliminar_pelicula, name="eliminar_pelicula"
    ),
    path("agregar_pelicula/", views.agregar_pelicula, name="agregar_pelicula"),
]
