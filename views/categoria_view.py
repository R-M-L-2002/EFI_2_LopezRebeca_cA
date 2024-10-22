from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.categoria_service import CategoriaService

categoria_bp = Blueprint('categoria', __name__)
categoria_service = CategoriaService()

@categoria_bp.route('/categorias')
def listar_categorias():
    categorias = categoria_service.listar_categorias()
    return render_template('categorias.html', categorias=categorias)

@categoria_bp.route('/categoria/nueva', methods=['GET', 'POST'])
def nueva_categoria():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre es requerido', 'error')
        else:
            categoria_service.crear_categoria(nombre)
            flash('Categoría creada con exito', 'success')
            return redirect(url_for('categoria.listar_categorias'))
    return render_template('categoria_form.html')

@categoria_bp.route('/categoria/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = categoria_service.listar_categorias().get(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre es requerido', 'error')
        else:
            categoria_service.editar_categoria(id, nombre)
            flash('Categoría actualizada con exito', 'success')
            return redirect(url_for('categoria.listar_categorias'))
    return render_template('categoria_form.html', categoria=categoria)

@categoria_bp.route('/categoria/borrar/<int:id>', methods=['POST'])
def borrar_categoria(id):
    categoria_service.eliminar_categoria(id)
    flash('Categoría eliminada con exito', 'success')
    return redirect(url_for('categoria.listar_categorias'))
