from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = [
            "titulo",
            "director",
            "sinopsis",
            "duracion",
            "clasificacion",
            "genero",
            "fecha_estreno",
            "imagen",
        ]
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                    "placeholder": "Título de la película",
                }
            ),
            "director": forms.TextInput(
                attrs={
                    "class": "w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                    "placeholder": "Nombre del director",
                }
            ),
            "sinopsis": forms.Textarea(
                attrs={
                    "class": "w-full resize-y rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                    "placeholder": "Escribe la sinopsis de la película...",
                    "rows": 5,
                }
            ),
            "duracion": forms.NumberInput(
                attrs={
                    "class": "w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                    "placeholder": "Duración en minutos",
                }
            ),
            "clasificacion": forms.Select(
                attrs={
                    "class": "w-full cursor-pointer rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                }
            ),
            "genero": forms.Select(
                attrs={
                    "class": "w-full cursor-pointer rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                }
            ),
            "fecha_estreno": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                    "class": "w-full cursor-pointer rounded-lg border border-slate-700 bg-slate-900 px-4 py-3 text-slate-200 outline-none transition focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500",
                },
            ),
            "imagen": forms.FileInput(
                attrs={
                    "class": "w-full cursor-pointer rounded-lg border border-slate-700 bg-slate-900 text-sm text-slate-400 transition file:mr-4 file:border-0 file:bg-indigo-600 file:px-4 file:py-3 file:font-semibold file:text-white hover:file:bg-indigo-500 file:cursor-pointer",
                }
            ),
        }
