
from collections import UserList
from socket import fromshare
from django import forms





class ArticuloForm(forms.Form):
    
    titulo=forms.CharField(max_length=30)
    texto=forms.CharField(max_length=1000)
    fecha=forms.DateField()


class AutorForm(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=1000)
    profesion=forms.CharField(max_length=30)


class SeccionForm(forms.Form):
    
    titulo=forms.CharField(max_length=30)
    
    
'''
class UserRegiterForm(UserCreationForm):
    
    email = forms.EmailField()
    password_1 = forms.CharField(label = "password", widget = forms.PasswordInput)
    password_2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = UserList
        fields = ["username", "email", "password_1", "password_2"]
        help_texts = {k:"" for k in fields}
'''  
        
        
        
