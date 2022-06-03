from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth.decorators import permission_required

from django.contrib.auth import authenticate, login

from .forms import ProductoForm, RegistroForm

from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'registro/index.html')


@permission_required('productos.add_producto')
def agregar_producto(request):
    #Cargamos el formulario en el data
    data = {
        'form': ProductoForm()
    }
    #verificamos el método enviado por el formulario
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


@permission_required("productos.view_producto")
def listar_productos(request):
    data = {
        'productos': Producto.objects.all()
    }
    return render(request, 'registro/listar.html', data)


@permission_required('productos.change_producto')
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


@permission_required('perms.producto.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect(to='listar_productos')


def registro(request):
    data = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='index')
        else:
            data['form'] = formulario
    return render(request, 'registration/register.html', data)



    
 