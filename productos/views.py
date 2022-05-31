from django.shortcuts import redirect, render, get_object_or_404

#importamos el formulario

from .forms import ProductoForm

from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'registro/index.html')

def agregar_producto(request):
    #Cargamos el formulario en el data
    data = {
        'form': ProductoForm()
    }
    #verificamos el metodo enviado por el formulario
    if request.method == 'POST':
        #Cargamos el formulario con los datos enviados
        formulario = ProductoForm(request.POST)
        #Verificamos que el formulario es valido
        if formulario.is_valid():
            #Guardamos el formulario
            formulario.save()
            #Redireccionamos a la pagina de listar productos
            return redirect('listar_productos')
        else:
            #Si el formulario no es valido, lo cargamos de nuevo
            data['form'] = formulario
    #Si el metodo no es POST, cargamos el formulario vacio
    return render(request, 'registro/agregar.html' , data)

def listar_productos(request):
    data = {
        'productos': Producto.objects.all()
    }
    return render(request, 'registro/listar.html', data)

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_productos')
        else:
            data['form'] = formulario

    return render(request, 'registro/editar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect(to='listar_productos')

    
