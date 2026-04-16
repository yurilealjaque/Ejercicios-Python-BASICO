"""pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito, haciendo que se reduzca el saldo_pagar.
mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
Crea el archivo un Python con la clase Usuario, con la base que te proporcionamos
Agrega el método pagar_tarjeta a la clase Usuario
Agrega el método mostrar_saldo_usuario a la clase Usuario
Crea 3 instancias de la clase Usuario
Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo
Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo
Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo"""

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
  
    def hacer_compra(self, monto):
        self.saldo_pagar += monto
        print(f"{self.nombre} realizó una compra de: ${monto}")

    def pagar_tarjeta(self, monto):
        # Reduce el saldo a pagar
        self.saldo_pagar -= monto
        print(f"{self.nombre} realizó un pago de: ${monto}")

    def mostrar_saldo_usuario(self):
        # Imprime el nombre completo y el saldo actual
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):
        # El usuario actual reduce su deuda, el otro la aumenta
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto
        print(f"--- Transferencia: {self.nombre} transfirió ${monto} de deuda a {otro_usuario.nombre} ---")

# --- Instancias y Operaciones ---

# 1. Crear 3 instancias
usuario1 = Usuario("pepe", "apellido1", "1@.com")
usuario2 = Usuario("Daniel", "apellido2", "2@com")
usuario3 = Usuario("Johnny", "apellido3", "3@.com")

print("--- Operaciones Usuario 1 ---")
# El primer usuario hace 2 compras y luego paga su tarjeta. Muestra su saldo.
usuario1.hacer_compra(5000)
usuario1.hacer_compra(3000)
usuario1.pagar_tarjeta(2000)
usuario1.mostrar_saldo_usuario()

print("\n--- Operaciones Usuario 2 ---")
# El segundo usuario hace 1 compra y luego paga 2 veces su tarjeta. Muestra su saldo.
usuario2.hacer_compra(10000)
usuario2.pagar_tarjeta(3000)
usuario2.pagar_tarjeta(2000)
usuario2.mostrar_saldo_usuario()

print("\n--- Operaciones Usuario 3 ---")
# El tercer usuario hace 3 compras y luego paga su tarjeta 4 veces. Muestra su saldo.
usuario3.hacer_compra(1000)
usuario3.hacer_compra(2000)
usuario3.hacer_compra(500)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(500)
usuario3.mostrar_saldo_usuario()

# Ejemplo opcional del BONUS
# usuario1.transferir_deuda(usuario3, 1000)
# usuario1.mostrar_saldo_usuario()
# usuario3.mostrar_saldo_usuario()