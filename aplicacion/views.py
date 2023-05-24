from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Movie
from .models import Vista
from .models import Comentario
from .models import Favorito

# pandas
import pandas as pd
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def top_movies(movie_id, movies_similarity_df):
    if movie_id in movies_similarity_df.columns:
        return movies_similarity_df[movie_id].sort_values(ascending=False).index[1:4]  
    else:
        return []


def top_users(user, user_similarity_df):
    similar_users_list = []
    similar_users = user_similarity_df.sort_values(by=user, ascending=False)
    for rank, similar_user in enumerate(similar_users, start=1):
        # Excluir al propio usuario objetivo
        if similar_user == user:
            continue

        similarity_score = user_similarity_df.loc[user, similar_user]
        if similarity_score > 0.3:
            similar_users_list.append(similar_user)
    return similar_users_list

def get_unseen_movies(target_user, similar_users, pivote2):
    unseen_movies = set()
    target_user_movies = set(pivote2.columns[pivote2.loc[target_user] == 1])

    for user in similar_users:
        user_movies = set(pivote2.columns[pivote2.loc[user] == 1])
        unseen_movies.update(user_movies.difference(target_user_movies))

    return unseen_movies

def recommend_movies(target_user, user_similarity_df, user_movie_df):
    similar_users = top_users(target_user, user_similarity_df)
    unseen_movies = get_unseen_movies(target_user, similar_users, user_movie_df)

    return unseen_movies
    
def get_data_model():
    movies = Movie.objects.values()
    views = Vista.objects.values()

    df_movies = pd.DataFrame(movies)
    df_views = pd.DataFrame(views)
    print(df_movies.columns)
    print(df_views.columns)
    df = df_views.merge(df_movies, left_on='idmovie_id',right_on='id')
    df = df[['idusuario_id','idmovie_id','rating','title']]

    data_model = df.pivot_table(index='idusuario_id', columns='idmovie_id',values='rating',aggfunc=np.mean)
    data_model.fillna(0,inplace=True)

    user_movie_df = data_model.copy()
    user_movie_df = user_movie_df.applymap(lambda x: 1 if x != 0 else 0)

    sparse_ratings=sp.sparse.csr_matrix(data_model.values)

    user_similarity = cosine_similarity(sparse_ratings)
    movies_similarity = cosine_similarity(sparse_ratings.T)

    user_similarity_df=pd.DataFrame(user_similarity, index=data_model.index, columns=data_model.index)
    movies_similarity_df=pd.DataFrame(movies_similarity, index=data_model.columns, columns=data_model.columns)

    return user_similarity_df, movies_similarity_df, user_movie_df


# Create your views here.
@login_required
def home(request):
<<<<<<< HEAD
    user = request.user
    movies = Movie.objects.all()[:10]
    favoritos = Favorito.objects.filter(idusuario_id=user.id).values_list('idmovie_id', flat=True)# flat minimiza la busqeuda extrayendo solo el valor en vez de una lista

    datos = {
        'user': user,
        'movies': movies,
        'favoritos': favoritos,
    }

    return render(request, 'Home/home.html', datos)
=======
    user=request.user
    movie=Movie.objects.all()[:10]

    user_similarity_df, movies_similarity_df, user_movie_df = get_data_model()
    ids_recomended_movies = recommend_movies(user.id, user_similarity_df, user_movie_df)
    movies_recomended = Movie.objects.filter(pk__in=list(ids_recomended_movies)[:15])
    print(len(movies_recomended))
    print(ids_recomended_movies)
    datos={
        'user':user,
        'movie':movie,
        'movies_recomended': movies_recomended
    }

    return render(request,'Home/home.html', datos)
>>>>>>> 2a2c4fddc07cbb63abbc6ef27777d4c34b5b7fa6


def views_movie(request, movie):
    movie = Movie.objects.get(id=movie)
    user = request.user
    idusuario = user.id

    #comentarios
    comentario= Comentario.objects.filter(idmovie_id=movie).all()
    favoritos = Favorito.objects.filter(idusuario_id=user.id).values_list('idmovie_id', flat=True)
    usuarios = []
    for comentarios in comentario:
        usuario = comentarios.idusuario
        usuarios.append(usuario)

    #modelo
    user_similarity_df, movies_similarity_df, user_movie_df = get_data_model()
    ids_recomended_movies = top_movies(movie.id,movies_similarity_df)
    print(ids_recomended_movies)
    movies_recomended = Movie.objects.filter(pk__in=list(ids_recomended_movies)[:15])

    try:
        visto=True
        comen=True
        calif=True
        datos={
            'movie':movie,
            'visto':visto,
            'comentario':comentario,
            'comen':comen,
            'usuarios':usuarios,
            'calif': calif,
<<<<<<< HEAD
            'favoritos':favoritos
=======
            'movies_recomended': movies_recomended
>>>>>>> 2a2c4fddc07cbb63abbc6ef27777d4c34b5b7fa6

        }
        vista = Vista.objects.get(idmovie_id=movie.id, idusuario_id=idusuario)
        return render(request, 'VerPelicula/views_movie.html', datos)


    except Vista.DoesNotExist:
  
        datos={
<<<<<<< HEAD
           
            'movie': movie,
            'favoritos':favoritos
=======
            'comen':comen,
            'movie': movie,
            'movies_recomended': movies_recomended
>>>>>>> 2a2c4fddc07cbb63abbc6ef27777d4c34b5b7fa6
            
        }
        return render(request, 'VerPelicula/views_movie.html', datos)


def calificar_pelicula(request,movie):
    user = request.user
    if request.method == 'POST':
        calificacion = request.POST.get('calificacion')
        print(calificacion)
        calificar=Vista(idmovie_id=movie,idusuario_id=user.id,rating=calificacion)
        calificar.save() 

        return redirect('views_movie', movie=movie)
    
    return JsonResponse({'error': 'Método de solicitud no válido.'}, status=400)       

def agregar_comentario(request,movie):
    user = request.user
    comentario=Comentario(comentario=request.POST['comentario'],idusuario_id=user.id,idmovie_id=movie)
    comentario.save()
    
    return redirect('views_movie', movie=movie)

def salir(request):
    logout(request)
    return redirect('/')

    
def buscar_pelicula(request):
    movie = Movie.objects.filter(title=request.POST['pelicula']).first()
    try:
        if movie:
            busqueda = True
            datos = {
                'movie': movie,
                'busqueda': busqueda
            }
            return render(request, 'Home/home.html', datos)
        else:
            raise Movie.DoesNotExist
    except Movie.DoesNotExist:
        error_message = 'No se encontró ninguna película con ese título.'
        return render(request, 'Home/homeerror.html', {'error_message': error_message})


def vista_favoritos(request):
    user = request.user
    favoritos = Favorito.objects.filter(idusuario_id=user.id).all()
    movies = []
    for favorito in favoritos:
        movie = Movie.objects.get(id=favorito.idmovie_id)
        movies.append(movie)
    return render(request, 'Favoritos/favoritos.html', {'movies': movies})

def quitar_favoritos(request,movie):
    user = request.user
    favoritos = Favorito.objects.filter(idusuario_id=user.id, idmovie_id=movie)

    if favoritos.exists():
        favoritos.delete()
    return redirect('vista_favoritos')    

def favorita_pelicula(request, movie):
    user = request.user
    favoritos = Favorito.objects.filter(idusuario_id=user.id, idmovie_id=movie)

    if favoritos.exists():
        favoritos.delete()
    else:
        favorito = Favorito(idmovie_id=movie, idusuario_id=user.id)
        favorito.save()

    return redirect('home')

def favorita_pelicula_vista(request, movie):
    user = request.user
    favoritos = Favorito.objects.filter(idusuario_id=user.id, idmovie_id=movie)

    if favoritos.exists():
        favoritos.delete()
    else:
        favorito = Favorito(idmovie_id=movie, idusuario_id=user.id)
        favorito.save()

    return redirect('views_movie', movie=movie)    
        

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']


        user = User.objects.create_user(username=username, password=password)

        user.first_name = nombre
        user.last_name = apellido
        user.email = correo


        user.save()


        return redirect('/')

    return render(request,'registration/register.html')



    