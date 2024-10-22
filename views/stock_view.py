from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.stock_service import StockService
from models import Equipo

stock_bp = Blueprint('stock', __name__)
stock_service = StockService()

@stock_bp.route('/stocks')
def listar_stocks():
    stocks = stock_service.listar_stocks()
    return render_template('stocks.html', stocks=stocks)

@stock_bp.route('/stock/nuevo', methods=['GET', 'POST'])
def nuevo_stock():
    equipos = Equipo.query.all()
    if request.method == 'POST':
        cantidad = request.form.get('cantidad')
        ubicacion = request.form.get('ubicacion')
        equipo_id = request.form.get('equipo_id')
        if not cantidad or not ubicacion or not equipo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            stock_service.crear_stock(cantidad, ubicacion, equipo_id)
            flash('Stock creado con exito', 'success')
            return redirect(url_for('stock.listar_stocks'))
    return render_template('stock_form.html', equipos=equipos)

@stock_bp.route('/stock/editar/<int:id>', methods=['GET', 'POST'])
def editar_stock(id):
    stock = stock_service.repository.get_by_id(id)
    equipos = Equipo.query.all()
    if request.method == 'POST':
        cantidad = request.form.get('cantidad')
        ubicacion = request.form.get('ubicacion')
        equipo_id = request.form.get('equipo_id')
        if not cantidad or not ubicacion or not equipo_id:
            flash('Todos los campos son requeridos', 'error')
        else:
            stock_service.editar_stock(id, cantidad, ubicacion, equipo_id)
            flash('Stock actualizado con exito', 'success')
            return redirect(url_for('stock.listar_stocks'))
    return render_template('stock_form.html', stock=stock, equipos=equipos)

@stock_bp.route('/stock/borrar/<int:id>', methods=['POST'])
def borrar_stock(id):
    stock_service.eliminar_stock(id)
    flash('Stock eliminado con exito', 'success')
    return redirect(url_for('stock.listar_stocks'))
