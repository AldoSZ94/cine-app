from django.db import models


class Pelicula(models.Model):

    class Clasificacion(models.TextChoices):
        AA = "AA", "AA"
        A = "A", "A"
        B = "B", "B"
        B15 = "B15", "B15"
        C = "C", "C"
        D = "D", "D"

    class Genero(models.TextChoices):
        ACCION = "accion", "Acción"
        COMEDIA = "comedia", "Comedia"
        DRAMA = "drama", "Drama"
        TERROR = "terror", "Terror"
        CIENCIA_FICCION = "ciencia_ficcion", "Ciencia ficción"
        ANIMACION = "animacion", "Animación"

    titulo = models.CharField("Título", max_length=200)
    director = models.CharField("Director", max_length=100)
    sinopsis = models.TextField("Sinópsis")
    duracion = models.PositiveIntegerField("Duración", help_text="Duración en minutos")
    clasificacion = models.CharField(
        "Clasificación", max_length=5, choices=Clasificacion.choices
    )
    genero = models.CharField("Género", max_length=20, choices=Genero.choices)
    fecha_estreno = models.DateField("Fecha de estreno")
    imagen = models.ImageField("Imagen", upload_to="peliculas/", blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
