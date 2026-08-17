# 🎬 Cine - Catálogo de Películas

**Cine** es una aplicación web desarrollada con Django que funciona como un catálogo interactivo de películas. El objetivo principal del proyecto es ofrecer una interfaz limpia, intuitiva y visual donde los usuarios puedan explorar una colección cinematográfica, consultar detalles relevantes de cada título y gestionar el contenido de forma organizada.

## 🌐 Demo

[Visitar CineApp](https://cine-app-qpzy.onrender.com)

## 🛠️ Tecnologías

- **Backend:** Python / Django.
- **Frontend:** HTML5, CSS3, Tailwind CSS, JavaScript.

## ✨ Funcionalidades principales

### 👤 Autenticación de usuarios

- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Inicio de sesión automático después del registro.
- Validaciones de contraseña mediante `UserCreationForm`.
- Acceso protegido a las operaciones del catálogo.
- Cada usuario administra únicamente sus propias películas.

### 🎬 Gestión de películas

- Crear nuevas películas.
- Consultar información detallada.
- Editar películas existentes.
- Eliminar películas mediante una pantalla de confirmación.
- Registro de fecha de creación y última actualización.
- Clasificación por edad y género.
- Carga opcional de imágenes.

### 🔎 Búsqueda y paginación

- Búsqueda de películas por título.
- Resultados filtrados según el usuario autenticado.
- Paginación del catálogo con **3 películas por página**.

### 🎨 Interfaz

- Diseño responsive.
- Tema oscuro.
- Interfaz construida con Tailwind CSS.
- Formularios personalizados.
- Estados `hover` y `focus`.
- Transiciones y efectos visuales.
- Mensajes de éxito, error, advertencia e información mediante el sistema de mensajes de Django.

### 💬 Mensajes dinámicos

Los mensajes generados por Django cuentan con un pequeño comportamiento adicional mediante **JavaScript vanilla**:

1. Aparecen progresivamente.
2. Permanecen visibles durante unos segundos.
3. Desaparecen mediante una transición.
4. Finalmente son eliminados del DOM.

## 📚 Lo que aprendí

Con este proyecto practiqué y reforcé conceptos como:

- Creación de modelos y relaciones mediante `ForeignKey`.
- Uso del sistema de autenticación integrado de Django.
- `ModelForm` y personalización de widgets.
- Operaciones CRUD.
- Protección de vistas mediante `login_required`.
- Filtrado de información según el usuario autenticado.
- Búsqueda con `icontains`.
- Paginación mediante `Paginator`.
- Manejo de archivos e imágenes con `ImageField` y Pillow.
- Sistema de mensajes de Django.
- Herencia de plantillas mediante `{% extends %}` y `{% block %}`.
- Manejo de archivos estáticos y multimedia.
- Integración de Tailwind CSS con Django.
- JavaScript para mejorar la experiencia de usuario.
- Preparación de una aplicación Django para despliegue.

## 🎯 Objetivo del proyecto

El proyecto fue creado como una práctica para llevar los conocimientos de Django más allá de ejemplos básicos, construyendo una aplicación con **autenticación, persistencia de datos, CRUD, búsqueda, paginación, carga de imágenes y despliegue**.

## 👨‍💻 Autor

**Aldo Sandoval Zepeda**

Proyecto desarrollado como parte de mi aprendizaje y práctica en desarrollo web con Python y Django.
