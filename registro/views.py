from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'registro/index.html')
    
def register(request):
    return render(request, 'registro/registro.html')

def login(request):
    return render(request, 'registro/login.html')
