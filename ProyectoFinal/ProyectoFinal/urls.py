"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import ver_inicio, procesar_autor, procesar_articulo, procesar_seccion
from blog.views import (
    formulario_borrar,
    formulario_buscar,
    editar_perfil,
    busqueda,
    login,
    logout,
    login_request,
    registro,
    inicio,
)

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("proyectofinal/", include("proyectofinal.urls")),
    path('ver_inicio/', ver_inicio),
    path('f-autor/', procesar_autor ),
    path('f-articulo/', procesar_articulo),
    path('f-seccion/', procesar_seccion),
    path('formulario_buscar/', formulario_buscar),
    path('formulario_borrar/', formulario_borrar),
    path('editar_perfil/', editar_perfil),
    path('ve_inicio/',ver_inicio),
    path('inicio/',inicio),
    path('login/', views.login_request, name = "Login"),
    path('registro/', views.registro, name = "Registro"),
    path('logout/', LogoutView.as_view(template_name = "blog/logout.html"), name = "Logout"),
    path('login_request/',login_request),
    
]
    
