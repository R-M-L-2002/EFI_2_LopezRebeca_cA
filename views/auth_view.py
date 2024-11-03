from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from schemas import UserSchema, UserMinimalSchema
from app import db
from flask_jwt_extended import jwt_required, get_jwt

# Definición del Blueprint para vistas de autenticación y administración de usuarios
auth_view_bp = Blueprint('auth_view', __name__)

@auth_view_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    """Inicia sesión del usuario. Verifica las credenciales y establece la sesión."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('auth_view.lista_usuarios'))
        else:
            flash('Credenciales incorrectas.')
    
    return render_template('login.html')

@auth_view_bp.route('/register', methods=['GET', 'POST'])
def register_view():
    """Registra un nuevo usuario con un nombre de usuario y contraseña hasheada."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Crear el usuario con `is_admin` establecido como False
        new_user = User(username=username, password_hash=hashed_password, is_admin=False)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Usuario registrado con éxito.')
        return redirect(url_for('auth_view.login_view'))

    return render_template('register.html')

@auth_view_bp.route('/usuarios', methods=['GET'])
def lista_usuarios():
    """Lista todos los usuarios. Solo accesible para administradores."""
    if not session.get('is_admin'):
        flash('No tienes permisos para acceder a esta página.')
        return redirect(url_for('auth_view.login_view'))

    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@auth_view_bp.route('/admin', methods=['GET', 'POST'])
def admin_view():
    """Vista de administración para crear usuarios. Solo accesible para administradores."""
    if not session.get('is_admin'):
        flash('No tienes permisos para acceder a esta página.')
        return redirect(url_for('auth_view.login_view'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario creado con éxito.')

    usuarios = User.query.all()
    return render_template('admin.html', usuarios=usuarios)

@auth_view_bp.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Elimina un usuario. Solo accesible para administradores."""
    if not session.get('is_admin'):
        flash('No tienes permisos para eliminar usuarios.')
        return redirect(url_for('auth_view.admin_view'))

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Usuario eliminado con éxito.')
    return redirect(url_for('auth_view.admin_view'))

@auth_view_bp.route('/users', methods=['GET'])
@jwt_required()
def users():
    """Devuelve una lista de usuarios. Incluye datos adicionales si el usuario es administrador."""
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    usuarios = User.query.all()
    
    if administrador:
        return UserSchema().dump(usuarios, many=True)
    else:
        return UserMinimalSchema().dump(usuarios, many=True)
