from repositories.inventario_repository import InventarioRepository
from models import Inventario

class InventarioService:
    def __init__(self):
        self.repository = InventarioRepository()

    def listar_inventarios(self):
        return self.repository.get_all()

    def crear_inventario(self, nombre, proveedor_id, cantidad, fecha):
        nuevo_inventario = Inventario(nombre=nombre, proveedor_id=proveedor_id, cantidad=cantidad, fecha=fecha)
        self.repository.add(nuevo_inventario)

    def editar_inventario(self, inventario_id, nombre, proveedor_id, cantidad, fecha):
        inventario = self.repository.get_by_id(inventario_id)
        if inventario:
            inventario.nombre = nombre
            inventario.proveedor_id = proveedor_id
            inventario.cantidad = cantidad
            inventario.fecha = fecha
            self.repository.update()

    def eliminar_inventario(self, inventario_id):
        inventario = self.repository.get_by_id(inventario_id)
        if inventario:
            self.repository.delete(inventario)
