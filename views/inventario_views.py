from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.inventario_service import InventarioService

inventario_bp = Blueprint('inventario', __name__)
inventario_service = InventarioService()

@inventario_bp.route('/inventarios')
def listar_inventarios():
    inventarios = inventario_service.listar_inventarios()
    return render_template('inventarios.html', inventarios=inventarios)

@inventario_bp.route('/inventario/nuevo', methods=['GET', 'POST'])
def nuevo_inventario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        proveedor_id = request.form.get('proveedor_id')
        cantidad = request.form.get('cantidad')
        fecha = request.form.get('fecha')
        
        if not nombre or not proveedor_id or not cantidad or not fecha:
            flash('Todos los campos son requeridos', 'error')
        else:
            inventario_service.crear_inventario(nombre, proveedor_id, cantidad, fecha)
            flash('Inventario creado con éxito', 'success')
            return redirect(url_for('inventario.listar_inventarios'))
    
    return render_template('inventario_form.html')

@inventario_bp.route('/inventario/editar/<int:id>', methods=['GET', 'POST'])
def editar_inventario(id):
    inventario = inventario_service.repository.get_by_id(id)
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        proveedor_id = request.form.get('proveedor_id')
        cantidad = request.form.get('cantidad')
        fecha = request.form.get('fecha')
        
        if not nombre or not proveedor_id or not cantidad or not fecha:
            flash('Todos los campos son requeridos', 'error')
        else:
            inventario_service.editar_inventario(id, nombre, proveedor_id, cantidad, fecha)
            flash('Inventario actualizado con éxito', 'success')
            return redirect(url_for('inventario.listar_inventarios'))
    
    return render_template('inventario_form.html', inventario=inventario)

@inventario_bp.route('/inventario/borrar/<int:id>', methods=['POST'])
def borrar_inventario(id):
    inventario_service.eliminar_inventario(id)
    flash('Inventario eliminado con éxito', 'success')
    return redirect(url_for('inventario.listar_inventarios'))
