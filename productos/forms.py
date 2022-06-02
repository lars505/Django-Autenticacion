#importamos el modelo del producto
from .models import Producto
from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    # nombre = forms.charField(widget.TextInput(attrs={'class':'form-control'}))
    # descripción = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 20}))
    class Meta:
        model = Producto
        fields = ('nombre', 'precio','descripcion', 'stock', 'categoria')
        #fields = '__all__'
        widgets = {     
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
   
        