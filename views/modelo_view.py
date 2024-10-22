from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.modelo_service import ModeloService
from models import Fabricante

modelo_bp = Blueprint('modelo', __name__)
modelo_service = ModeloService()

@modelo_bp.route('/modelos')
def listar_modelos():
    modelos = modelo_service.listar_modelos()
    return render_template('listar_modelos.html', modelos=modelos)

@modelo_bp.route('/modelo/crear', methods=['GET', 'POST'])
def crear_modelo():
    fabricantes = Fabricante.query.all()
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fabricante_id = request.form.get('fabricante_id')
        if not nombre or not fabricante_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            modelo_service.crear_modelo(nombre, fabricante_id)
            flash('Modelo creado con exito', 'success')
            return redirect(url_for('modelo.listar_modelos'))
    return render_template('crear_modelo.html', fabricantes=fabricantes)

@modelo_bp.route('/modelo/editar/<int:id>', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = modelo_service.listar_modelos().get(id)
    fabricantes = Fabricante.query.all()
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fabricante_id = request.form.get('fabricante_id')
        if not nombre or not fabricante_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            modelo_service.editar_modelo(id, nombre, fabricante_id)
            flash('Modelo actualizado con exito', 'success')
            return redirect(url_for('modelo.listar_modelos'))
    return render_template('editar_modelo.html', modelo=modelo, fabricantes=fabricantes)

@modelo_bp.route('/modelo/eliminar/<int:id>', methods=['POST'])
def eliminar_modelo(id):
    modelo_service.eliminar_modelo(id)
    flash('Modelo eliminado con exito', 'success')
    return redirect(url_for('modelo.listar_modelos'))
