from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Usuarios registrados (simulado en memoria)
USUARIOS = {
    'admin': 'admin123',
    'usuario': 'pass123',
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username in USUARIOS and USUARIOS[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard.index'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm  = request.form.get('confirm', '').strip()

        if not username or not password:
            flash('Todos los campos son obligatorios.', 'danger')
        elif password != confirm:
            flash('Las contraseñas no coinciden.', 'danger')
        elif username in USUARIOS:
            flash('El usuario ya existe.', 'warning')
        else:
            USUARIOS[username] = password
            flash('Usuario registrado correctamente. Inicia sesión.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
