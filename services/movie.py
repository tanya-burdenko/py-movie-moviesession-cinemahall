from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(genres__in=genres_ids, actors__in=actors_ids)
    if genres_ids is not None:
        return Movie.objects.filter(genres__in=genres_ids)
    if actors_ids is not None:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int):
    return Movie.objects.filter(id=movie_id)


def create_movie(title: str, description: str, genres_ids: List[int], actors_ids: List[int]):
    new_movie = Movie.objects.create(
        title=title,
        description=description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie