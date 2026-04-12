"""El Problema: Una tienda ofrece descuentos según el monto de compra.

Menos de 100$: Sin descuento.
Entre 100$ y 500$: 5% de descuento.
Más de 500$: 10% de descuento. Escribe un script que calcule el precio final."""


compra = float(input("introduce el monto de la compra: "))
descuento = 0

if compra < 100:
    descuento= 0
elif compra <= 500: 
    descuento= 0.25

else:
    descuento= 0.10

precio_final = compra - (compra * descuento)
print(f"El precio final a pagar es: ${precio_final}")
