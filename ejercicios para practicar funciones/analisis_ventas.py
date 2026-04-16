import pandas as pd

# 1. Carga de datos (tu lista de diccionarios original)
ventas_data = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 800.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 800.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 25.0}
]

# Convertimos la lista a un DataFrame (una tabla de Pandas)
df = pd.DataFrame(ventas_data)

# Añadimos columna de ingresos por línea
df['ingresos'] = df['cantidad'] * df['precio']

# --- PROCESAMIENTO AUTOMÁTICO ---

# A. Ingresos totales
ingresos_totales = df['ingresos'].sum()

# B. Ventas por producto (agrupación)
resumen_por_producto = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingresos': 'sum',
    'precio': 'mean'
}).rename(columns={'precio': 'precio_promedio'})

# C. Ingresos por día
ingresos_por_dia = df.groupby('fecha')['ingresos'].sum()

# --- GENERACIÓN DEL ARCHIVO DE ENTREGA ---

with pd.ExcelWriter('Reporte_Ventas_Final.xlsx') as writer:
    # Hoja 1: Datos Originales
    df.to_excel(writer, sheet_name='Datos Originales', index=False)
    
    # Hoja 2: Resumen por Producto
    resumen_por_producto.to_excel(writer, sheet_name='Resumen Productos')
    
    # Hoja 3: Ingresos por Día
    ingresos_por_dia.to_excel(writer, sheet_name='Ingresos por Dia')

print(f"Análisis completado. Ingreso total global: ${ingresos_totales}")
print("Archivo 'Reporte_Ventas_Final.xlsx' generado con éxito.")