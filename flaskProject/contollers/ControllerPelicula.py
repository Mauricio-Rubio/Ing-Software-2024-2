from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from model.model_pelicula import *

from flask import Blueprint, render_template

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def ver_peliculas():
    peliculas = get_peliculas()
    return render_template('pelicula_template.html', peliculas=peliculas)

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        duracion = request.form.get('duracion') or None
        inventario = request.form.get('inventario') or None
        if not nombre or not genero:
            flash('Favor de llenar todos los campos', 'danger')
            return redirect(url_for('pelicula.agregar_pelicula'))
        add_pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        flash('Película agregada correctamente', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))
    return render_template('pelicula_agregar.html')

@pelicula_blueprint.route('/eliminar_pelicula/<int:pelicula_id>', methods=['POST'])
def eliminar_pelicula(pelicula_id):
    success = del_pelicula_by_id(pelicula_id)
    if success:
        flash('Película eliminada correctamente', 'success')
    else:
        flash('No se pudo eliminar la película', 'danger')
    return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/editar/<int:pelicula_id>', methods=['GET', 'POST'])
def actualizar_pelicula(pelicula_id):
    pelicula = search_pelicula_by_id(pelicula_id)
    if not pelicula:
        flash('No se encontró la película', 'danger')
        return redirect(url_for('pelicula.ver_peliculas'))
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        duracion = request.form.get('duracion') or None
        inventario = request.form.get('inventario') or None
        if not nombre or not genero:
            flash('Favor de llenar todos los campos', 'danger')
            return redirect(url_for('pelicula.actualizar_pelicula'))
        if duracion and int(duracion) < 0 or inventario and int(inventario) < 0:
            flash('La duración no puede ser negativa', 'danger')
            return redirect(url_for('pelicula.actualizar_pelicula', pelicula_id=pelicula_id))
        update_pelicula_by_id(pelicula_id, nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        flash('Película actualizada correctamente', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))
    return render_template('pelicula_editar.html', pelicula_id=pelicula.idPelicula, pelicula=pelicula)