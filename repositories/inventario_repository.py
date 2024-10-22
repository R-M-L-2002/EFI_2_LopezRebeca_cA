from models import Inventario
from app import db

class InventarioRepository:
    def get_all(self):
        return Inventario.query.all()

    def get_by_id(self, inventario_id):
        return Inventario.query.get(inventario_id)

    def add(self, inventario):
        db.session.add(inventario)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, inventario):
        db.session.delete(inventario)
        db.session.commit()
