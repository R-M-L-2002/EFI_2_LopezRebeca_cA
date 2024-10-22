from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.venta_service import VentaService
from models import Cliente, Equipo

venta_bp = Blueprint('venta', __name__)
venta_service = VentaService()

@venta_bp.route('/ventas')
def listar_ventas():
    ventas = venta_service.listar_ventas()
    return render_template('ventas.html', ventas=ventas)

@venta_bp.route('/venta/nuevo', methods=['GET', 'POST'])
def nuevo_venta():
    clientes = Cliente.query.all()
    equipos = Equipo.query.all()
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        equipo_id = request.form.get('equipo_id')
        precio = request.form.get('precio')
        fecha = request.form.get('fecha')
        if not cliente_id or not equipo_id or not precio or not fecha:
            flash('Todos los campos son requeridos', 'error')
        else:
            venta_service.crear_venta(cliente_id, equipo_id, precio, fecha)
            flash('Venta creada con exito', 'success')
            return redirect(url_for('venta.listar_ventas'))
    return render_template('venta_form.html', clientes=clientes, equipos=equipos)

@venta_bp.route('/venta/editar/<int:id>', methods=['GET', 'POST'])
def editar_venta(id):
    venta = venta_service.repository.get_by_id(id)
    clientes = Cliente.query.all()
    equipos = Equipo.query.all()
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        equipo_id = request.form.get('equipo_id')
        precio = request.form.get('precio')
        fecha = request.form.get('fecha')
        if not cliente_id or not equipo_id or not precio or not fecha:
            flash('Todos los campos son requeridos', 'error')
        else:
            venta_service.editar_venta(id, cliente_id, equipo_id, precio, fecha)
            flash('Venta actualizada con exito', 'success')
            return redirect(url_for('venta.listar_ventas'))
    return render_template('venta_form.html', venta=venta, clientes=clientes, equipos=equipos)

@venta_bp.route('/venta/borrar/<int:id>', methods=['POST'])
def borrar_venta(id):
    venta_service.eliminar_venta(id)
    flash('Venta eliminada con exito', 'success')
    return redirect(url_for('venta.listar_ventas'))
