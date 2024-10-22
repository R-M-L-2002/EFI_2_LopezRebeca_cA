import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------    

from views.marca_view import marca_bp
app.register_blueprint(marca_bp)

from views.fabricante_view import fabricante_bp
app.register_blueprint(fabricante_bp)

from views.auth_view import auth_bp
app.register_blueprint(auth_bp)

from views.categoria_view import categoria_bp
app.register_blueprint(categoria_bp)

from views.caracteristica_view import caracteristica_bp
app.register_blueprint(caracteristica_bp)

from views.stock_view import stock_bp
app.register_blueprint(stock_bp)

from views.proveedor_view import proveedor_bp
app.register_blueprint(proveedor_bp)

from views.accesorio_view import accesorio_bp
app.register_blueprint(accesorio_bp)

from views.equipo_view import equipo_bp
app.register_blueprint(equipo_bp)

from views.inventario_views import inventario_bp
app.register_blueprint(inventario_bp)

from views.cliente_views import cliente_bp
app.register_blueprint(cliente_bp)

from views.venta_views import venta_bp
app.register_blueprint(venta_bp)

from views.user_views import user_bp
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)