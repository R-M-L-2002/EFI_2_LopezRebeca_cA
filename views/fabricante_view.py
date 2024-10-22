from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.fabricante_service import FabricanteService

fabricante_bp = Blueprint('fabricante', __name__)
fabricante_service = FabricanteService()

@fabricante_bp.route('/fabricantes')
def listar_fabricantes():
    fabricantes = fabricante_service.listar_fabricantes()
    return render_template('listar_fabricantes.html', fabricantes=fabricantes)

@fabricante_bp.route('/fabricante/crear', methods=['GET', 'POST'])
def crear_fabricante():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        pais_origen = request.form.get('pais_origen')
        if not nombre or not pais_origen:
            flash('Todos los campos son requeridos', 'error')
        else:
            fabricante_service.crear_fabricante(nombre, pais_origen)
            flash('Fabricante creado con exito', 'success')
            return redirect(url_for('fabricante.listar_fabricantes'))
    return render_template('crear_fabricante.html')

@fabricante_bp.route('/fabricante/editar/<int:id>', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = fabricante_service.listar_fabricantes().get(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        pais_origen = request.form.get('pais_origen')
        if not nombre or not pais_origen:
            flash('Todos los campos son requeridos', 'error')
        else:
            fabricante_service.editar_fabricante(id, nombre, pais_origen)
            flash('Fabricante actualizado con exito', 'success')
            return redirect(url_for('fabricante.listar_fabricantes'))
    return render_template('editar_fabricante.html', fabricante=fabricante)

@fabricante_bp.route('/fabricante/eliminar/<int:id>', methods=['POST'])
def eliminar_fabricante(id):
    fabricante_service.eliminar_fabricante(id)
    flash('Fabricante eliminado con exito', 'success')
    return redirect(url_for('fabricante.listar_fabricantes'))
