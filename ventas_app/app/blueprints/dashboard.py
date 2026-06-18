from flask import Blueprint, render_template, redirect, url_for, session
from app.utils import (cargar_datos, calcular_kpis, ventas_por_categoria,
                       ventas_por_mes, ventas_por_metodo_pago,
                       ventas_por_sucursal, top_productos)

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@dashboard_bp.route('/')
@login_required
def index():
    datos = cargar_datos()
    kpis = calcular_kpis(datos)
    cat   = ventas_por_categoria(datos)
    meses = ventas_por_mes(datos)
    metodos = ventas_por_metodo_pago(datos)
    sucursales = ventas_por_sucursal(datos)
    productos = top_productos(datos, 10)
    tabla = datos[-20:][::-1]  # últimas 20 ventas

    return render_template('dashboard/index.html',
                           kpis=kpis,
                           cat_labels=list(cat.keys()),
                           cat_values=list(cat.values()),
                           mes_labels=list(meses.keys()),
                           mes_values=list(meses.values()),
                           metodo_labels=list(metodos.keys()),
                           metodo_values=list(metodos.values()),
                           sucursal_labels=list(sucursales.keys()),
                           sucursal_values=list(sucursales.values()),
                           prod_labels=list(productos.keys()),
                           prod_values=list(productos.values()),
                           tabla=tabla,
                           usuario=session.get('user'))


@dashboard_bp.route('/tabla')
@login_required
def tabla_completa():
    datos = cargar_datos()
    return render_template('dashboard/tabla.html',
                           datos=datos,
                           usuario=session.get('user'))
