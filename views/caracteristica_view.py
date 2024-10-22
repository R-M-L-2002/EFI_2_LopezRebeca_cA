from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.caracteristica_service import CaracteristicaService
from models import Modelo

caracteristica_bp = Blueprint('caracteristica', __name__)
caracteristica_service = CaracteristicaService()

@caracteristica_bp.route('/caracteristicas')
def listar_caracteristicas():
    caracteristicas = caracteristica_service.listar_caracteristicas()
    return render_template('caracteristicas.html', caracteristicas=caracteristicas)

@caracteristica_bp.route('/caracteristica/nueva', methods=['GET', 'POST'])
def nueva_caracteristica():
    modelos = Modelo.query.all()
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        descripcion = request.form.get('descripcion')
        modelo_id = request.form.get('modelo_id')
        if not tipo or not descripcion or not modelo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            caracteristica_service.crear_caracteristica(tipo, descripcion, modelo_id)
            flash('Característica creada con éxito', 'success')
            return redirect(url_for('caracteristica.listar_caracteristicas'))
    return render_template('caracteristica_form.html', modelos=modelos)

@caracteristica_bp.route('/caracteristica/editar/<int:id>', methods=['GET', 'POST'])
def editar_caracteristica(id):
    caracteristica = caracteristica_service.repository.get_by_id(id)
    modelos = Modelo.query.all()
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        descripcion = request.form.get('descripcion')
        modelo_id = request.form.get('modelo_id')
        if not tipo or not descripcion or not modelo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            caracteristica_service.editar_caracteristica(id, tipo, descripcion, modelo_id)
            flash('Característica actualizada con éxito', 'success')
            return redirect(url_for('caracteristica.listar_caracteristicas'))
    return render_template('caracteristica_form.html', caracteristica=caracteristica, modelos=modelos)

@caracteristica_bp.route('/caracteristica/borrar/<int:id>', methods=['POST'])
def borrar_caracteristica(id):
    caracteristica_service.eliminar_caracteristica(id)
    flash('Característica eliminada con éxito', 'success')
    return redirect(url_for('caracteristica.listar_caracteristicas'))