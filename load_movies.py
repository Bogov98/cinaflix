import csv
from aplicacion.models import Movie

with open('data_movie.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la fila de encabezados si existe
    for row in reader:
        _, created = Movie.objects.get_or_create(
            id=row[0],
            title=row[1],
            vote_average=row[2],
            release_date=row[3],
            imdb_id=row[4],
            generos=row[5],
            poster_link=row[6],
        )
