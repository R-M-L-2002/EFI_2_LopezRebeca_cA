from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.accesorio_service import AccesorioService
from models import Modelo

accesorio_bp = Blueprint('accesorio', __name__)
accesorio_service = AccesorioService()

@accesorio_bp.route('/accesorios')
def listar_accesorios():
    accesorios = accesorio_service.listar_accesorios()
    return render_template('accesorios.html', accesorios=accesorios)

@accesorio_bp.route('/accesorio/nuevo', methods=['GET', 'POST'])
def nuevo_accesorio():
    modelos = Modelo.query.all()  
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        modelo_id = request.form.get('modelo_id')
        if not tipo or not modelo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            accesorio_service.crear_accesorio(tipo, modelo_id)
            flash('Accesorio creado con exito', 'success')
            return redirect(url_for('accesorio.listar_accesorios'))
    return render_template('accesorio_form.html', modelos=modelos)

@accesorio_bp.route('/accesorio/editar/<int:id>', methods=['GET', 'POST'])
def editar_accesorio(id):
    accesorio = accesorio_service.repository.get_by_id(id)
    modelos = Modelo.query.all() 
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        modelo_id = request.form.get('modelo_id')
        if not tipo or not modelo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            accesorio_service.editar_accesorio(id, tipo, modelo_id)
            flash('Accesorio actualizado con exito', 'success')
            return redirect(url_for('accesorio.listar_accesorios'))
    return render_template('accesorio_form.html', accesorio=accesorio, modelos=modelos)

@accesorio_bp.route('/accesorio/borrar/<int:id>', methods=['POST'])
def borrar_accesorio(id):
    accesorio_service.eliminar_accesorio(id)
    flash('Accesorio eliminado con exito', 'success')
    return redirect(url_for('accesorio.listar_accesorios'))
