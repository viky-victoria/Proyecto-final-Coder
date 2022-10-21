from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Autor, Seccion, Articulo

from blog.forms import ArticuloForm, AutorForm, SeccionForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def ver_inicio(request):
    return render (request, "blog/ver_inicio.html")



def inicio(request):
    return render (request, "blog/inicio.html")



def procesar_autor(request):
    if request.method =="GET":
        mi_formulario= AutorForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/f-autor.html", context=contexto)
    
    if request.method =="POST":
        mi_formulario= AutorForm(request.POST)
        if mi_formulario.is_valid():
            dato_ingresado= mi_formulario.cleaned_data
            nuevo_modelo= Autor(
                nombre= dato_ingresado["nombre"],
                apellido= dato_ingresado["apellido"],
                fecha= dato_ingresado["fecha"],
            )
            nuevo_modelo.save()
            
            return render(request, "blog/exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "blog/f-autor.html", context=contexto)
    


def procesar_articulo(request):
        
    if request.method =="GET":
        mi_formulario= ArticuloForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/f-articulo.html", context=contexto)
    
    if request.method =="POST":
        mi_formulario= ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            dato_ingresado= mi_formulario.cleaned_data
            nuevo_modelo= Articulo(
                titulo= dato_ingresado["titulo"],
                texto= dato_ingresado["texto"],
                fecha= dato_ingresado["fecha"],
            )
            nuevo_modelo.save()
            
            return render(request, "blog/exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "blog/f-articulo.html", context=contexto)
    
        

def procesar_seccion(request):
    if request.method =="GET":
        mi_formulario= SeccionForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/f-seccion.html", context=contexto)
    
    if request.method =="POST":
        mi_formulario= SeccionForm(request.POST)
        if mi_formulario.is_valid():
            dato_ingresado= mi_formulario.cleaned_data
            nuevo_modelo= Seccion(
                titulo= dato_ingresado["titulo"],
                texto= dato_ingresado["texto"],
                fecha= dato_ingresado["fecha"],
            )
            nuevo_modelo.save()
            
            return render(request, "blog/exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "blog/f-seccion.html", context=contexto)
     
        

def formulario_buscar(request):
    
    return render(request, "blog/formulario_buscar.html")



def formulario_borrar(request):
    
    return render(request, "blog/formulario_borrar.html")


def busqueda(request):
    
    return render(request, "blog/busqueda.html")



def editar_perfil(request):
    
    return render(request, "blog/editar_perfil.html")



def login(request):

    return render(request, "blog/login.html")



from django.contrib.auth.views import LoginView


class MyLogin(LoginView):
    template_name = "blog/login.html"
    
    


def logout(request):
    
    return render(request, "blog/logout.html")
