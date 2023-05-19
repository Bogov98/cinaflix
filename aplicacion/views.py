from django.shortcuts import render
from.models import Movie

def menu(request):
    movies=Movie.objects.all() [:10]
    return render(request,'menu/menupeliculas.html',{'movies':movies})



