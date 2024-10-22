from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/usuarios')
def listar_usuarios():
    usuarios = user_service.listar_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@user_bp.route('/usuario/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'user')
        if not username or not password:
            flash('El nombre de usuario y la contraseña son requeridos', 'error')
        else:
            user_service.crear_usuario(username, password, role)
            flash('Usuario creado con exito', 'success')
            return redirect(url_for('user.listar_usuarios'))
    return render_template('usuario_form.html')

@user_bp.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = user_service.repository.get_by_id(id)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        if not username:
            flash('El nombre de usuario es requerido', 'error')
        else:
            user_service.editar_usuario(id, username, password, role)
            flash('Usuario actualizado con exito', 'success')
            return redirect(url_for('user.listar_usuarios'))
    return render_template('usuario_form.html', usuario=usuario)

@user_bp.route('/usuario/borrar/<int:id>', methods=['POST'])
def borrar_usuario(id):
    user_service.eliminar_usuario(id)
    flash('Usuario eliminado con exito', 'success')
    return redirect(url_for('user.listar_usuarios'))
