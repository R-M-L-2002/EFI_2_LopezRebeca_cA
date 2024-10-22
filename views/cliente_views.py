from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.cliente_service import ClienteService

cliente_bp = Blueprint('cliente', __name__)
cliente_service = ClienteService()

@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = cliente_service.listar_clientes()
    return render_template('clientes.html', clientes=clientes)

@cliente_bp.route('/cliente/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre es requerido', 'error')
        else:
            cliente_service.crear_cliente(nombre)
            flash('Cliente creado con exito', 'success')
            return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente_form.html')

@cliente_bp.route('/cliente/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = cliente_service.repository.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre es requerido', 'error')
        else:
            cliente_service.editar_cliente(id, nombre)
            flash('Cliente actualizado con exito', 'success')
            return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente_form.html', cliente=cliente)

@cliente_bp.route('/cliente/borrar/<int:id>', methods=['POST'])
def borrar_cliente(id):
    cliente_service.eliminar_cliente(id)
    flash('Cliente eliminado con exito', 'success')
    return redirect(url_for('cliente.listar_clientes'))
