# 🎬 Cine - Catálogo de Películas

**Cine** es una aplicación web desarrollada con Django que funciona como un catálogo interactivo de películas. El objetivo principal del proyecto es ofrecer una interfaz limpia, intuitiva y visual donde los usuarios puedan explorar una colección cinematográfica, consultar detalles relevantes de cada título y gestionar el contenido de forma organizada.

---

## 💡 Concepto y Funcionalidad del Proyecto

La aplicación resuelve la necesidad de centralizar y presentar un catálogo de películas con sus respectivos datos informativos e imágenes de portada (pósters).

### Funcionalidades clave:

- **Exploración visual:** Galería con tarjetas que presentan los pósters y datos principales de cada película.
- **Ficha técnica individual:** Vista de detalle por película que incluye sinopsis completa, categoría/género, año de estreno y duración.
- **Gestión dinámica de imágenes:** Manejo de archivos multimedia (`MEDIA`) para cargar y mostrar los pósters de forma nativa desde la base de datos.
- **Control de estado vacío (Empty State):** Mensajes interactivos y sugerencias cuando el catálogo no contiene películas registradas.
- **Panel de administración:** Integración con el sistema de administración de Django para crear, editar o eliminar películas de manera rápida y segura.

---

## 🖥️ Descripción de las Vistas y Navegación

El flujo de navegación de la aplicación está diseñado en torno a tres experiencias principales:

### 1. Vista Principal (Catálogo / Listado)

Es la página de aterrizaje de la aplicación.

- **Propósito:** Mostrar todas las películas disponibles en el catálogo en una cuadrícula responsiva.
- **Elementos en pantalla:**
  - Tarjetas informativas con el póster, título, categoría y año de cada producción.
  - Efectos visuales de interacción (_hover_) en las imágenes y enlaces para invitar a la navegación.
  - Cláusula de estado vacío (_empty state_) con un mensaje amistoso si la base de datos no contiene registros.

### 2. Vista de Detalle de Película

Página dedicada a mostrar la información completa de una película seleccionada.

- **Propósito:** Brindar la ficha técnica y la sinopsis del título.
- **Elementos en pantalla:**
  - Póster en mayor resolución.
  - Metadatos destacados (Año de lanzamiento, Género/Categoría, Duración).
  - Sinopsis o descripción argumental detallada.
  - Botón de retorno al catálogo principal.

### 3. Panel de Administración (Gestión de Contenido)

Interfaz reservada para la administración del sistema.

- **Propósito:** Administrar la base de datos del catálogo sin necesidad de modificar código.
- **Acciones disponibles:**
  - Alta de nuevas películas con subida de imágenes/pósters.
  - Modificación de metadatos existentes.
  - Eliminación de registros.

---

## 🛠️ Tecnologías y Estilos

- **Backend:** Python / Django (Views basadas en funciones, ORM de Django, gestión de archivos `MEDIA`).
- **Frontend:** HTML5 semántico, CSS3 y **Tailwind CSS** para un diseño moderno, fluido y adaptable a dispositivos móviles.
- **Base de Datos:** SQLite.
