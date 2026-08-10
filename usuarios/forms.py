from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    # Personaliza los campos del formulario.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "class": "w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20",
                "placeholder": "Ingresa tu nombre de usuario",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": "w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20",
                "placeholder": "Ingresa tu contraseña",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20",
                "placeholder": "Confirma tu contraseña",
            }
        )
