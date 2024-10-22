from repositories.venta_repository import VentaRepository
from models import Venta

class VentaService:
    def __init__(self):
        self.repository = VentaRepository()

    def listar_ventas(self):
        return self.repository.get_all()

    def crear_venta(self, cliente_id, equipo_id, precio, fecha):
        nueva_venta = Venta(cliente_id=cliente_id, equipo_id=equipo_id, precio=precio, fecha=fecha)
        self.repository.add(nueva_venta)

    def editar_venta(self, venta_id, cliente_id, equipo_id, precio, fecha):
        venta = self.repository.get_by_id(venta_id)
        if venta:
            venta.cliente_id = cliente_id
            venta.equipo_id = equipo_id
            venta.precio = precio
            venta.fecha = fecha
            self.repository.update()

    def eliminar_venta(self, venta_id):
        venta = self.repository.get_by_id(venta_id)
        if venta:
            self.repository.delete(venta)
