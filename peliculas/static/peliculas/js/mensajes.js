const mensaje = document.querySelector("#mensaje");

// Maneja los mensajes de Django.
if (mensaje) {
  const esperar = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  async function mostrarYEliminarMensaje() {
    await esperar(100);
    mensaje.classList.replace("opacity-0", "opacity-100");
    await esperar(3000);
    mensaje.classList.replace("opacity-100", "opacity-0");
    await esperar(1000);
    mensaje.remove();
  }

  mostrarYEliminarMensaje();
}
