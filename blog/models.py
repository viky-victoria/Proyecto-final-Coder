from ast import For
from pyexpat import model
from tabnanny import verbose
from tkinter import Widget
from turtle import width
from django.db import models
# from blog.views import formulario_borrar
# from blog.views import registro

# Create your models here.

class  Autor(models.Model):
    class Meta:
        verbose_name_plural= "Autores"
        
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    profesion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre   

class  Articulo(models.Model):
    class Meta:
        verbose_name_plural= "Articulos"

    titulo=models.CharField(max_length=30)
    texto=models.CharField(max_length=1000)
    fecha=models.DateField(null=True)
    
    def __str__(self):
        return self.titulo   


class Seccion(models.Model):
    class Meta:
        verbose_name_plural= "Secciones"
       
    nombre=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre   
    



    