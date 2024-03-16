from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from model.model_usuario import *

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def ver_usuario():
    usuarios = get_usuarios()
    print(usuarios)
    return render_template('usuario_template.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apPat = request.form.get('apPat') or None
        apMat = request.form.get('apMat') or None
        password = request.form.get('password') or None
        email = request.form.get('email') or None
        profilePicture = request.form.get('profilePicture') or None
        superUser = request.form.get('superUser') or None
        if not nombre or not apPat or not apMat or not password:
            flash('Favor de llenar todos los campos', 'danger')
            return redirect(url_for('usuario.agregar_usuario'))
        add_usuario(nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, profilePicture=profilePicture, superUser=superUser)
        flash('Usuario agregado correctamente', 'success')
        return redirect(url_for('usuario.ver_usuario'))
    return render_template('usuario_agregar.html')

@usuario_blueprint.route('/eliminar_usuario/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    success = del_usuario_by_id(usuario_id)
    if success:
        flash('Usuario eliminado correctamente', 'success')
    else:
        flash('No se pudo eliminar el usuario', 'danger')
    return redirect(url_for('usuario.ver_usuario'))

@usuario_blueprint.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def actualizar_usuario(usuario_id):
    usuario = search_usuario_by_id(usuario_id)
    if not usuario:
        flash('No se encontró el usuario', 'danger')
        return redirect(url_for('usuario.ver_usuario'))
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apPat = request.form.get('apPat') or None
        apMat = request.form.get('apMat') or None
        password = request.form.get('password') or None
        email = request.form.get('email') or None
        profilePicture = request.form.get('profilePicture') or None
        superUser = request.form.get('superUser') or None
        if not nombre or not apPat or not apMat or not password:
            flash('Favor de llenar todos los campos', 'danger')
            return redirect(url_for('usuario.actualizar_usuario', usuario_id=usuario_id))
        update_usuario_by_id(usuario_id, nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, profilePicture=profilePicture, superUser=superUser)
        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('usuario.ver_usuario'))
    return render_template('usuario_editar.html', usuario_id=usuario.idUsuario, usuario=usuario)