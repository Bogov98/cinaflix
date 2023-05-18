from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User



# Create your views here.
@login_required
def home(request):
    usuario= request.user
    print(usuario)
    return render(request,'Home/home.html')

def salir(request):
    logout(request)
    return redirect('/')

    


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']

        # Crear un nuevo objeto de usuario
        user = User.objects.create_user(username=username, password=password)

        # Actualizar los campos personalizados del usuario
        user.first_name = nombre
        user.last_name = apellido
        user.email = correo

        # Guardar el usuario en la base de datos
        user.save()

        # Redireccionar a la página de inicio de sesión
        return redirect('/')

    return render(request,'registration/register.html')