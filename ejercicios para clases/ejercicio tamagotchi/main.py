from tamagotchi import Tamagotchi, Mametchi
from persona import Persona

# 1. Crear la mascota (Instancia de Tamagotchi o la subclase Mametchi)
mi_mascota = Mametchi("Kuchipatchi", "Verde")

# 2. Crear la persona y asignarle la mascota
dueño = Persona("Ash", "Ketchum", mi_mascota)

# 3. Realizar acciones
print(f"--- Iniciando aventura con {dueño.nombre} ---")
dueño.darle_comida().curarlo().jugar_con_tamagotchi()