from django.core.exceptions import ObjectDoesNotExist
from aplicacion.models import Usuario, Movie, Vista  
import pandas as pd

def load_csv_into_db(csv_file_path):
    data = pd.read_csv(csv_file_path)
    
    for index, row in data.iterrows():
        user_id = row['userId']
        movie_id = row['movieId']
        rating = row['rating']
        
        try:
            usuario = Usuario.objects.get(idusuario=user_id)
            movie = Movie.objects.get(id=movie_id)
        except ObjectDoesNotExist:
            print(f"El usuario con ID {user_id} o la película con ID {movie_id} no existen en la base de datos. Se omite esta fila.")
            continue

        vista = Vista(idusuario=usuario, idmovie=movie, rating=rating)
        vista.save()

