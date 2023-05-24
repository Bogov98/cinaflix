from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.home, name='login'),
    path('salir',views.salir, name='salir'),
    path('home', views.home, name='home'),
    path('accounts/',include ('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('views_movie/<int:movie>/',views.views_movie, name='views_movie'),
    path('agregar_comentario/<int:movie>/',views.agregar_comentario, name='agregar_comentario'),
    path('buscar_pelicula/',views.buscar_pelicula, name='buscar_pelicula'),
    path('calificar_pelicula/<int:movie>/',views.calificar_pelicula, name='calificar_pelicula'),
    path('favorita_pelicula/<int:movie>/',views.favorita_pelicula, name='favorita_pelicula'),
    path('vista_favoritos/',views.vista_favoritos, name='vista_favoritos'),
    path('quitar_favoritos/<int:movie>/',views.quitar_favoritos, name='quitar_favoritos'),
    path('favorita_pelicula_vista/<int:movie>/',views.favorita_pelicula_vista, name='favorita_pelicula_vista'),


    

]