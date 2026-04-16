"""TarjetaCredito (Práctica)
Objetivos

Practicar las convenciones para crear clases
Implementar argumentos por default
Practicar las estructuras de control
Crear y actualizar los atributos de una instancia a través de self
Probar las funcionalidades de desarrollo a través de la creación de instancias e invocación de métodos
___________________________________________________________________________________________________-
La clase debe incluir los siguientes métodos:

compra(self, monto): aumenta el saldo_pagar de acuerdo al monto recibido siempre y cuando la tarjeta de crédito no haya llegado a su límite crediticio. De lo contrario, que imprima: “Tarjeta Rechazada, has alcanzado tu límite de crédito”.
pago(self, monto): disminuye el saldo_pagar de la tarjeta.
mostrar_info_tarjeta(self): imprime en la consola el saldo a pagar de la tarjeta. Por ejemplo: “Saldo a Pagar: $100”
cobrar_interes(self): aumenta el saldo_pagar cobrando intereses. Es decir al saldo_pagar actual se le agregará el saldo_pagar * los intereses.
_________________________________________________________________________________________________________
-Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses
-Crea el método compra para la clase TarjetaCredito
-Crea el método pago para la clase TarjetaCredito
-Crea el método mostrar_info_tarjeta para la clase TarjetaCredito
-Crea el método cobrar_interes para la clase TarjetaCredito
-Crea 3 tarjetas
-Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
-Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
-Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
-BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. En el capítulo pasado te dimos algunas pistas de cómo realizarlo.

"""

class TarjetaCredito:
    # Lista de clase para almacenar todas las instancias creadas (para el BONUS)
    todas_las_tarjetas = []

    def __init__(self, limite_credito, saldo_pagar=0, intereses=0.02):
        # Nota: Los argumentos con valores por default van al final
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        self.intereses = intereses
        # Agregamos la instancia a la lista de clase
        TarjetaCredito.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self # Permite encadenar

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self # Permite encadenar

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self # Permite encadenar

    def cobrar_interes(self):
        self.saldo_pagar += (self.saldo_pagar * self.intereses)
        return self # Permite encadenar

    @classmethod
    def imprimir_todas_las_tarjetas(cls):
        print("\n--- Información de todas las tarjetas ---")
        for tarjeta in cls.todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

# --- Creación de Instancias y Pruebas ---

# 1. Primera tarjeta: 2 compras, 1 pago, intereses y mostrar info
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.05)
print("Tarjeta 1:")
tarjeta1.compra(100).compra(200).pago(50).cobrar_interes().mostrar_info_tarjeta()

# 2. Segunda tarjeta: 3 compras, 2 pagos, intereses y mostrar info
tarjeta2 = TarjetaCredito(5000, 0, 0.03)
print("\nTarjeta 2:")
tarjeta2.compra(1000).compra(500).compra(300).pago(200).pago(100).cobrar_interes().mostrar_info_tarjeta()

# 3. Tercera tarjeta: 5 compras (exceder límite) y mostrar info
tarjeta3 = TarjetaCredito(500) # Límite bajo para probar el rechazo
print("\nTarjeta 3:")
tarjeta3.compra(100).compra(100).compra(100).compra(100).compra(200).mostrar_info_tarjeta()

# BONUS: Imprimir todas las instancias creadas
TarjetaCredito.imprimir_todas_las_tarjetas()