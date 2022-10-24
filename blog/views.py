from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Autor, Seccion, Articulo

from blog.forms import ArticuloForm, AutorForm, SeccionForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def ver_inicio(request):
    return render (request, "ver_inicio.html")



def procesar_autor(request):
    if request.method =="GET":
        mi_formulario= AutorForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "f-autor.html", context=contexto)
    
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
            
            return render(request, "exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "f-autor.html", context=contexto)
    


def procesar_articulo(request):
        
    if request.method =="GET":
        mi_formulario= ArticuloForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "f-articulo.html", context=contexto)
    
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
            
            return render(request, "exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "f-articulo.html", context=contexto)
    
        

def procesar_seccion(request):
    if request.method =="GET":
        mi_formulario= SeccionForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "f-seccion.html", context=contexto)
    
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
            
            return render(request, "exito.html")
        contexto={"formulario": mi_formulario}
        return render(request, "f-seccion.html", context=contexto)
     
        

def formulario_buscar(request):
    
    return render(request, "formulario_buscar.html")



def formulario_borrar(request):
    
    return render(request, "formulario_borrar.html")


def busqueda(request):
    
    return render(request, "busqueda.html")



def editar_perfil(request):
    
    return render(request, "editar_perfil.html")



def login(request):

    return render(request, "login.html")



def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get("Username")
            password = form.cleaned_data.get("Password")
            
            user = authenticate(username=user, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, "ver_inicio.html", {"mensaje": f"Bienvenido/a {user}"})
            else:
                return render(request, "ver_inicio.html", {"mensaje": "ERROR, Datos incorrectos"})
        else:
                return render(request, "ver_inicio.html", {"mensaje": "ERROR, Formulario incorrecto"})
    
    form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})



def registro(request):
     if request.method == "POST":
         
        form = UserCreationForm(request.POST)         
        if form.is_valid():
            
            user = form.cleaned.data["Username"]
            form.save()
            return render(request, "ver_inicio.html", {"Mensaje:" "Usuario creado"})
         
        
        else:
        
            form = UserCreationFrom()
            #form = UserRegisterForm()
        
        return render(request, "registro.html", {"form":form})
    
    


def logout(request):
    
    return render(request, "logout.html")
