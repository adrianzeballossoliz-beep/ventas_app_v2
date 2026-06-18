import csv
import os
from collections import defaultdict

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'ventas_supermercado.csv')


def cargar_datos():
    """Carga y retorna todas las filas del CSV."""
    datos = []
    with open(CSV_PATH, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['cantidad'] = int(row['cantidad'])
            row['precio_unitario'] = float(row['precio_unitario'])
            row['total_venta'] = float(row['total_venta'])
            datos.append(row)
    return datos


def calcular_kpis(datos):
    total_ventas = sum(r['total_venta'] for r in datos)
    cantidad_total = sum(r['cantidad'] for r in datos)
    promedio_venta = total_ventas / len(datos) if datos else 0

    ventas_por_categoria = defaultdict(float)
    for r in datos:
        ventas_por_categoria[r['categoria']] += r['total_venta']
    categoria_top = max(ventas_por_categoria, key=ventas_por_categoria.get) if ventas_por_categoria else '-'

    return {
        'total_ventas': round(total_ventas, 2),
        'cantidad_total': cantidad_total,
        'promedio_venta': round(promedio_venta, 2),
        'categoria_top': categoria_top,
        'num_registros': len(datos),
    }


def ventas_por_categoria(datos):
    agg = defaultdict(float)
    for r in datos:
        agg[r['categoria']] += r['total_venta']
    return dict(sorted(agg.items(), key=lambda x: x[1], reverse=True))


def ventas_por_mes(datos):
    agg = defaultdict(float)
    for r in datos:
        mes = r['fecha'][:7]  # YYYY-MM
        agg[mes] += r['total_venta']
    return dict(sorted(agg.items()))


def ventas_por_metodo_pago(datos):
    agg = defaultdict(float)
    for r in datos:
        agg[r['metodo_pago']] += r['total_venta']
    return dict(sorted(agg.items(), key=lambda x: x[1], reverse=True))


def ventas_por_sucursal(datos):
    agg = defaultdict(float)
    for r in datos:
        agg[r['sucursal']] += r['total_venta']
    return dict(sorted(agg.items(), key=lambda x: x[1], reverse=True))


def top_productos(datos, n=10):
    agg = defaultdict(float)
    for r in datos:
        agg[r['producto']] += r['total_venta']
    return dict(sorted(agg.items(), key=lambda x: x[1], reverse=True)[:n])
