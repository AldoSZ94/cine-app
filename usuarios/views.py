from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm


# Autenticación de usuarios.
def login_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        # Si las credenciales son correctas, inicia sesión.
        if user is not None:
            login(request, user)
            messages.success(request, "¡Has iniciado sesión de forma exitosa!")
            return redirect("peliculas:lista_peliculas")
        messages.error(
            request, "El usuario o contraseña son incorrectos. Vuelve a intentarlo."
        )
    return render(request, "authentication/login.html")


# Cierre de sesión.
def logout_usuario(request):
    logout(request)
    messages.success(request, ("¡Tu sesión fue cerrada de forma exitosa!"))
    return redirect("peliculas:lista_peliculas")


# Registro de nuevos usuarios.
def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            # Inicia sesión automáticamente después del registro.
            login(request, user)
            messages.success(request, "¡Te has registrado de forma exitosa!")
            return redirect("peliculas:lista_peliculas")
    else:
        form = RegistroUsuarioForm()
    return render(request, "authentication/registro_usuario.html", {"form": form})
