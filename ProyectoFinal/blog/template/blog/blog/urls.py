from django.contrib import admin
from django.urls import path, include

# from blog.views import ver_inicio, procesar_autor, procesar_articulo, procesar_seccion
# from blog.views import (
#     formulario_borrar,
#     formulario_buscar,
#     editar_perfil,
#     busqueda,
#     login,
#     logout,
#     login_request,
#     registro,
#     inicio,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    # path("proyectofinal/", include("proyectofinal.urls")),
    # path('ver_inicio/', ver_inicio),
    # path('f-autor/', procesar_autor ),
    # path('f-articulo/', procesar_articulo),
    # path('f-seccion/', procesar_seccion),
    # path('formulario_buscar/', formulario_buscar),
    # path('formulario_borrar/', formulario_borrar),
    # path('editar_perfil/', editar_perfil),
    # path('ve_inicio/',ver_inicio),
    # path('inicio/',inicio),
    # path('login/', views.login_request, name = "Login"),
    # path('registro/', views.registro, name = "Registro"),
    # path('logout/', LogoutView.as_view(template_name = "blog/logout.html"), name = "Logout"),
    # path('login_request/',login_request),
    
]
    