from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.marca_service import MarcaService

marca_bp = Blueprint('marca', __name__)
marca_service = MarcaService()

@marca_bp.route('/marcas')
def listar_marcas():
    marcas = marca_service.listar_marcas()
    return render_template('marcas.html', marcas=marcas)

@marca_bp.route('/marcas/crear', methods=['GET', 'POST'])
def crear_marca():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre es requerido', 'error')
        else:
            marca_service.crear_marca(nombre)
            flash('Marca creada con éxito', 'success')
            return redirect(url_for('marca.listar_marcas'))
    return render_template('crear_marca.html')

@marca_bp.route('/marcas/editar/<int:id>', methods=['GET', 'POST'])
def editar_marca(id):
    marca = marca_service.listar_marcas().get(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if nombre:
            marca_service.editar_marca(id, nombre)
            flash('Marca actualizada con éxito', 'success')
            return redirect(url_for('marca.listar_marcas'))
        flash('El nombre es requerido', 'error')
    return render_template('editar_marca.html', marca=marca)

@marca_bp.route('/marcas/eliminar/<int:id>', methods=['POST'])
def eliminar_marca(id):
    marca_service.eliminar_marca(id)
    flash('Marca eliminada con éxito', 'success')
    return redirect(url_for('marca.listar_marcas'))
