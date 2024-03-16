from alchemyClasses.Usuario import Usuario
from alchemyClasses import db


def search_usuario_by_id(id):
    return Usuario.query.filter(Usuario.idUsuario == id).first()

def get_usuarios(limit=None):
    if limit:
        return Usuario.query.limit(limit).all()
    return Usuario.query.all()

def update_usuario_by_id(id, **kwargs):
    usuario = search_usuario_by_id(id)
    for key, value in kwargs.items():
        if hasattr(usuario, key):
            setattr(usuario, key, value)
    db.session.commit()
    return usuario

def del_usuario_by_id(id, all=False):
    try:
        if all:
            Usuario.query.delete()
            db.session.commit()
        else:
            usuario = search_usuario_by_id(id)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
    except:
        return False
    return usuario

def add_usuario(**kwargs):
    try:
        usuario = Usuario(**kwargs)
        db.session.add(usuario)
        db.session.commit()
        return usuario
    except:
        return False
