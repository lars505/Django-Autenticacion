#importamos el modelo del producto
from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    # nombre = forms.charField(widget.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Producto
        #fields = ['nombre', 'precio','descripcion', 'stock', 'categoria']
        fields = '__all__'