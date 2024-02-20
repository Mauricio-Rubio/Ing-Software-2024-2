from alchemyClasses.Renta import Renta
from alchemyClasses import db


def search_renta_by_id(id):
    return Renta.query.filter(Renta.idRentar == id).first()


def get_all_rentas():
    return Renta.query.all()


def update_renta_by_id(id, **kwargs):
    renta = search_renta_by_id(id)
    for key, value in kwargs.items():
        if hasattr(renta, key):
            setattr(renta, key, value)
    db.session.commit()
    return renta


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
