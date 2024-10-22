from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserService.login_user(username, password)
        if user:

            return redirect(url_for('home'))  
        flash('Credenciales incorrectas')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        UserService.register_user(username, password)
        return redirect(url_for('auth.login'))  
    return render_template('register.html')
