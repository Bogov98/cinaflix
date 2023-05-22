from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Movie
from .models import Vista
from .models import Comentario



# Create your views here.
@login_required
def home(request):
    movie=Movie.objects.all()[:10]
    return render(request,'Home/home.html',{'movie':movie})


def views_movie(request, movie):
    movie = Movie.objects.get(id=movie)
    user = request.user
    idusuario = user.id

    #comentarios
    comentario= Comentario.objects.filter(idmovie_id=movie).all()
    usuarios = []

    for comentarios in comentario:
        usuario = comentarios.idusuario
        usuarios.append(usuario)

    try:
        visto=True
        comen=True
        datos={
            'movie':movie,
            'visto':visto,
            'comentario':comentario,
            'comen':comen,
            'usuarios':usuarios

        }
        vista = Vista.objects.get(idmovie_id=movie.id, idusuario_id=idusuario)
        return render(request, 'VerPelicula/views_movie.html', datos)


    except Vista.DoesNotExist:
        vistaInsert = Vista(idmovie_id=movie.id, idusuario_id=idusuario)
        vistaInsert.save()
        comen=True
        datos={
            'comen':comen,
            'movie': movie
            
        }
        return render(request, 'VerPelicula/views_movie.html', datos)

def agregar_comentario(request,movie):
    user = request.user
    comentario=Comentario(comentario=request.POST['comentario'],idusuario_id=user.id,idmovie_id=movie)
    comentario.save()
    movie = Movie.objects.get(id=movie)
    user = request.user
    idusuario = user.id
    comentario= Comentario.objects.filter(idmovie_id=movie).all()
    visto=True
    comen=True
    datos={
        'movie':movie,
        'visto':visto,
        'comentario':comentario,
        'comen':comen,
        'user':user

        }
    return render(request, 'VerPelicula/views_movie.html', datos)

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



    