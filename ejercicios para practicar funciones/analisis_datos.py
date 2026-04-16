# 1. Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 800.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 800.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 25.0}
]

# 2. Cálculo de Ingresos Totales
ingresos_totales_globales = 0
for venta in ventas:
    ingresos_totales_globales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    cant = venta["cantidad"]
    if prod not in ventas_por_producto:
        ventas_por_producto[prod] = 0
    ventas_por_producto[prod] += cant

# Identificar el más vendido
producto_top = None
max_cantidad = 0
for prod, cant in ventas_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        producto_top = prod

# 4. Promedio de Precio por Producto (Usando Tuplas)
precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    # ingresos_venta = cantidad * precio
    ingreso_venta = venta["cantidad"] * venta["precio"]
    cant = venta["cantidad"]
    
    if prod not in precios_por_producto:
        precios_por_producto[prod] = (0.0, 0)
    
    # Actualizamos la tupla: (suma_precios, cantidad_total)
    suma_actual, cant_actual = precios_por_producto[prod]
    precios_por_producto[prod] = (suma_actual + ingreso_venta, cant_actual + cant)

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    dia = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if dia not in ingresos_por_dia:
        ingresos_por_dia[dia] = 0.0
    ingresos_por_dia[dia] += ingreso

# 6. Representación de Datos (Resumen de Ventas)
resumen_ventas = {}
for prod in ventas_por_producto:
    suma_dinero, total_unidades = precios_por_producto[prod]
    resumen_ventas[prod] = {
        "cantidad_total": total_unidades,
        "ingresos_totales": suma_dinero,
        "precio_promedio": suma_dinero / total_unidades
    }

# --- IMPRESIÓN DE RESULTADOS PARA LA ENTREGA ---
print("--- REPORTE DE VENTAS ---")
print(f"Ingresos Totales: ${ingresos_totales_globales}")
print(f"Producto más vendido: {producto_top} ({max_cantidad} unidades)")
print("\nIngresos por día:")
for dia, monto in ingresos_por_dia.items():
    print(f"- {dia}: ${monto}")

print("\nResumen por Producto:")
for prod, info in resumen_ventas.items():
    print(f"[{prod.upper()}] Cantidad: {info['cantidad_total']} | "
          f"Ingresos: ${info['ingresos_totales']} | "
          f"Promedio: ${info['precio_promedio']:.2f}")