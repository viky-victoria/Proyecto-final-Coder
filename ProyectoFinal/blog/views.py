from multiprocessing import context
from django.shortcuts import render
#from django.http import HttpResponse

from blog.forms import ArticuloForm, AutorForm, SeccionForm
from blog.models import Articulo

# Create your views here.

def ver_inicio(request):
    return render (request, "blog/inicio.html")


def procesar_autor(request):
    mi_formulario= AutorForm()
    contexto= {"formulario": mi_formulario}
    return render(request, "blog/f-autor.html", context=contexto)


def procesar_articulo(request):
    
    breakpoint()
    
    if request.method =="GET":
        mi_formulario= ArticuloForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/f-articulo.html", context=contexto)
    
    if request.method =="POST":
        mi_formulario= ArticuloForm(request.POST)
        dato_ingresado= mi_formulario.cleaned_data
        nuevo_modelo= Articulo(
        titulo= dato_ingresado["texto"],
        texto= dato_ingresado["texto"],
        fecha= dato_ingresado["texto"],
        )
    nuevo_modelo.save()
        

def procesar_seccion(request):
    mi_formulario= SeccionForm()
    contexto= {"formulario": mi_formulario}
    return render(request, "blog/f-seccion.html", context=contexto)
