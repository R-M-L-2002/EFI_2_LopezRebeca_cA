from models import Venta
from app import db

class VentaRepository:
    def get_all(self):
        return Venta.query.all()

    def get_by_id(self, venta_id):
        return Venta.query.get(venta_id)

    def add(self, venta):
        db.session.add(venta)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, venta):
        db.session.delete(venta)
        db.session.commit()
