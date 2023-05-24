import csv
from django.contrib.auth.models import User
from aplicacion.models import Movie, Vista 

def import_data():
    with open('ratings_small.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Esto salta la primera fila (cabeceras)
        for row in reader:
            userId, movieId, rating = row
            try:
                user = User.objects.get(id=userId)
                movie = Movie.objects.get(id=movieId)
            except (User.DoesNotExist, Movie.DoesNotExist):
                continue
            Vista.objects.create(idusuario=user, idmovie=movie, rating=round(float(rating)))
    print("Data imported successfully")
