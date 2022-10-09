from django.contrib import admin
from blog.models import Autor, Articulo, Seccion

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor) 
admin.site.register(Seccion)