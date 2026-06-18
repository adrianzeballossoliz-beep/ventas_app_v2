# Sistema Web Demostrativo de Análisis de Ventas

Aplicación web Flask para el Examen Final de Programación Web.

## Estructura del Proyecto

```
ventas_app/
├── run.py                        # Archivo principal de ejecución
├── requirements.txt
├── ventas_supermercado.csv       # Dataset
├── app/
│   ├── __init__.py               # App factory + registro de blueprints
│   ├── utils.py                  # Lectura y procesamiento del CSV
│   ├── blueprints/
│   │   ├── auth.py               # Blueprint: login, register, logout
│   │   ├── dashboard.py          # Blueprint: dashboard y tabla
│   │   └── main.py               # Blueprint: redirección raíz
│   ├── static/
│   │   └── css/style.css         # Estilos personalizados
│   └── templates/
│       ├── base.html             # Template base (Bootstrap 5)
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── dashboard/
│       │   ├── index.html        # Dashboard con KPIs y gráficos
│       │   └── tabla.html        # Tabla completa de datos
│       └── main/
│           └── navbar.html       # Navbar reutilizable
```

## Cómo ejecutar

```bash
pip install -r requirements.txt
python run.py
```
Luego abrir: http://127.0.0.1:5000

Usuarios de prueba: admin / admin123  |  usuario / pass123

## Tecnologías

- Python + Flask (Blueprints, session, flash)
- HTML5, CSS3, Bootstrap 5
- Chart.js (4 gráficos: línea, dona, barras horizontales, barras)
- CSV con módulo estándar de Python

## KPIs del Dashboard

1. Total de Ventas (Bs.)
2. Cantidad total de productos vendidos
3. Promedio por venta
4. Categoría con mayor venta

## Gráficos

1. Ventas mensuales (línea)
2. Distribución por categoría (dona)
3. Métodos de pago (barras horizontales)
4. Top 10 productos (barras)
