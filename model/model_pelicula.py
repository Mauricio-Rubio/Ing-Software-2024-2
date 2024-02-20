from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db


def search_pelicula_by_id(id):
    return Pelicula.query.filter(Pelicula.idPelicula == id).first()


def get_all_peliculas():
    return Pelicula.query.all()


def update_pelicula_by_id(id, **kwargs):
    pelicula = search_pelicula_by_id(id)
    for key, value in kwargs.items():
        if hasattr(pelicula, key):
            setattr(pelicula, key, value)
    db.session.commit()
    return pelicula


def del_pelicula_by_id(id, all=False):
    try:
        if all:
            Pelicula.query.delete()
            db.session.commit()
        else:
            pelicula = search_pelicula_by_id(id)
            if pelicula:
                db.session.delete(pelicula)
                db.session.commit()
    except:
        return False
    return pelicula
