from django.urls import path
from django.conf import settings

from blog.views import ver_inicio,busqueda,procesar_autor,procesar_articulo,procesar_seccion,formulario_buscar,formulario_borrar,editar_perfil,login_request
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", ver_inicio, name="inicio"),  
    path("busqueda/", busqueda, name="busqueda"),
    path('f-autor/', procesar_autor , name="procesar_autor"),
    path('f-articulo/', procesar_articulo, name="procesar_articulo"),
    path('f-seccion/', procesar_seccion, name="procesar_seccion"),
    path('formulario_buscar/', formulario_buscar, name="formulario_buscar"),
    path('formulario_borrar/', formulario_borrar, name="formulario_borrar"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('logout/', LogoutView.as_view(template_name = "logout"), name = "Logout"),  
    path('login_request/',login_request,name="login_request"),  
]

