from datetime import timedelta, datetime
from alchemyClasses.Renta import Renta
from model.model_usuario import *
from model.model_pelicula import *
from alchemyClasses import db


def search_renta_by_id(id):
    return Renta.query.filter(Renta.idRentar == id).first()


def get_rentas(limit=None):
    if limit:
        return Renta.query.limit(limit).all()
    rents = Renta.query.all()
    for rent in rents:
        rent.fecha_entrega = rent.fecha_renta + timedelta(days=rent.dias_de_renta)
        rent.renta_vencida = rent.fecha_entrega < datetime.now()
    return rents


def update_renta_by_id(id, **kwargs):
    renta = search_renta_by_id(id)
    for key, value in kwargs.items():
        if hasattr(renta, key):
            setattr(renta, key, value)
    db.session.commit()
    return {"renta": renta, "message": "Renta actualizada correctamente"}

def del_renta_by_id(id, all=False):
    try:
        if all:
            Renta.query.delete()
            db.session.commit()
        else:
            renta = search_renta_by_id(id)
            if renta:
                db.session.delete(renta)
                db.session.commit()
    except:
        return False
    return renta

def add_renta(**kwargs):
    usuario = search_usuario_by_id(kwargs['idUsuario'])
    pelicula = search_pelicula_by_id(kwargs['idPelicula'])
    if not usuario:
        return {"renta": False, "message": "El usuario no existe"}
    if not pelicula:
        return {"renta": False, "message": "La película no existe"}
    renta = Renta(**kwargs)
    db.session.add(renta)
    db.session.commit()
    return {"renta": renta, "message": "Renta agregada correctamente"}
