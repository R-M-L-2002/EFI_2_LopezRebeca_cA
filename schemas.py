from app import ma

from datetime import date
from marshmallow import validates, ValidationError

from models import Marca, Fabricante, Modelo, Categoria, Caracteristica, Stock, Proveedor, Accesorio, Equipo, Inventario, Cliente, Venta, User

class MarcaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Marca

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class FabricanteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Fabricante
        
    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
    pais_origen = ma.auto_fields.Str(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class ModeloSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Modelo

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
    fabricante_id = ma.auto_fields.Int(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        
    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class CaracteristicaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Caracteristica

    id = ma.auto_fields.Int()
    tipo = ma.auto_fields.Str(required=True)
    descripcion = ma.auto_fields.Str(required=True)
    modelo_id = ma.auto_fields.Int(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class StockSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stock

    id = ma.auto_fields.Int()
    cantidad = ma.auto_fields.Int(required=True)
    ubicacion = ma.auto_fields.Str(required=True)
    equipo_id = ma.auto_fields.Int(required=True)
    disponible = ma.auto_fields.Bool()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
    contacto = ma.auto_fields.Str(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class AccesorioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Accesorio

    id = ma.auto_fields.Int()
    tipo = ma.auto_fields.Str(required=True)
    modelo_id = ma.auto_fields.Int(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class EquipoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Equipo

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
    precio = ma.auto_fields.Float(required=True)
    categoria_id = ma.auto_fields.Int(required=True)
    marca_id = ma.auto_fields.Int(required=True)
    modelo_id = ma.auto_fields.Int(required=True)
    caracteristica_id = ma.auto_fields.Int(required=True)
    accesorio_id = ma.auto_fields.Int(required=False)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class InventarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventario

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
    proveedor_id = ma.auto_fields.Int(required=True)
    cantidad = ma.auto_fields.Int(required=True)
    fecha = ma.auto_fields.Date(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente

    id = ma.auto_fields.Int()
    nombre = ma.auto_fields.Str(required=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class VentaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Venta

    id = ma.auto_fields.Int()
    cliente_id = ma.auto_fields.Int(required=True)
    equipo_id = ma.auto_fields.Int(required=True)
    usuario_id = ma.auto_fields.Int(required=True)
    precio = ma.auto_fields.Float(required=True)
    fecha = ma.auto_fields.DateTime()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

class UserSchema(ma.SQLAlchemyAutoSchema): 
    class Meta:
        model = User

    id = ma.auto_fields.Int()
    username = ma.auto_fields.Str(required=True)
    role = ma.auto_fields.Str(required=False)