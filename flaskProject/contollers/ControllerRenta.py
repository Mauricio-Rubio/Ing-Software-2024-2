from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from model.model_renta import *
from model.model_pelicula import *
from model.model_usuario import *

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/')
def ver_renta():
    rentas = get_rentas()
    print(rentas)
    for renta in rentas:
        print (renta.renta_vencida)
    return render_template('renta_template.html', rentas=rentas)

@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        idPelicula = request.form.get('idPelicula')
        idUsuario = request.form.get('idUsuario')
        fecha_renta = request.form.get('fecha_renta') or None
        dias_de_renta = request.form.get('dias_de_renta') or None
        estatus = request.form.get('estatus') or None
        if not idPelicula or not idUsuario or not fecha_renta:
            flash('Favor de llenar todos los campos', 'danger')
            return redirect(url_for('renta.agregar_renta'))
        renta = add_renta(idPelicula=idPelicula, idUsuario=idUsuario, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)
        if not renta.get('renta'):
            flash(renta['message'], 'danger')
            return redirect(url_for('renta.agregar_renta'))
        flash(renta['message'], 'success')
        return redirect(url_for('renta.ver_renta'))
    return render_template('renta_agregar.html')

@renta_blueprint.route('/eliminar_renta/<int:renta_id>', methods=['POST'])
def eliminar_renta(renta_id):
    success = del_renta_by_id(renta_id)
    if success:
        flash('Renta eliminada correctamente', 'success')
    else:
        flash('No se pudo eliminar la renta', 'danger')
    return redirect(url_for('renta.ver_renta'))

@renta_blueprint.route('/editar/<int:renta_id>', methods=['GET', 'POST'])
def actualizar_renta(renta_id):
    renta = search_renta_by_id(renta_id)
    if not renta:
        flash('No se encontró la renta', 'danger')
        return redirect(url_for('renta.ver_renta'))
    if request.method == 'POST':
        estatus = bool(request.form.get('estatus')) if request.form.get('estatus') != '0' else False
        renta = update_renta_by_id(renta_id, estatus=estatus)
        if not renta.get('renta') or not renta.get('estatus'):
            flash(renta['message'], 'danger')
            return redirect(url_for('renta.ver_renta'))
        flash(renta['message'], 'success')
        return redirect(url_for('renta.ver_renta'))
    return render_template('renta_editar.html', renta_id=renta.idRentar, renta=renta)