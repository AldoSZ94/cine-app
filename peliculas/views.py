from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PeliculaForm
from .models import Pelicula


def lista_peliculas(request):
    print("Hola")
    hay_busqueda = False
    pelicula_buscada = request.GET.get("pelicula_buscada")
    print("Buscando:", pelicula_buscada)
    if pelicula_buscada:
        peliculas = Pelicula.objects.filter(titulo__icontains=pelicula_buscada)
        hay_busqueda = True
    else:
        peliculas = Pelicula.objects.all()
    paginator = Paginator(peliculas, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "peliculas/lista_peliculas.html",
        {"page_obj": page_obj, "hay_busqueda": hay_busqueda},
    )


def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, "peliculas/detalle_pelicula.html", {"pelicula": pelicula})


@login_required()
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    datos = {
        "titulo": "Editar Película",
        "subtitulo": "Modifica la información de la película del catálogo.",
    }
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect("peliculas:lista_peliculas")
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, "peliculas/formulario.html", {"form": form, "datos": datos})


@login_required()
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        pelicula.delete()
        return redirect("peliculas:lista_peliculas")
    return render(request, "peliculas/eliminar_pelicula.html", {"pelicula": pelicula})


@login_required()
def agregar_pelicula(request):
    datos = {
        "titulo": "Agregar Película",
        "subtitulo": "Completa la información de la película para agregarla al catálogo.",
    }
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Película "{form.cleaned_data["titulo"]}" agregada al catálogo.',
            )
            return redirect("peliculas:lista_peliculas")
    else:
        form = PeliculaForm
    return render(request, "peliculas/formulario.html", {"form": form, "datos": datos})
