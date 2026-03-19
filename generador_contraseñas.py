import random, string

caracteres = list(string.ascii_letters + string.digits + "!#@%&*")

tam= int(input("Introduce un tamaño para la contraseña: "))

random.shuffle(caracteres)

password = []
for i in range(tam):
    password.append(random.choice(caracteres))

random.shuffle(password)

print("".join(password))



'''
import random, string # Importamos librerías para aleatoriedad y manejo de texto
random: Es la librería que permite generar aleatoriedad (elegir al azar o mezclar).
string: Es una librería que contiene constantes útiles, como todo el abecedario en una sola variable.

# Creamos una lista con letras (mayúsculas/minúsculas), números y símbolos
caracteres = list(string.ascii_letters + string.digits + "!#@%&*")

# Pedimos al usuario el largo de la contraseña y lo convertimos a entero (int)
tam = int(input("Introduce un tamaño para la contraseña: "))

# Mezclamos la lista de caracteres inicial para que no estén en orden alfabético
random.shuffle(caracteres)

password = [] # Lista vacía donde guardaremos los caracteres elegidos

# Un ciclo que se ejecutará 'tam' veces
for i in range(tam):
    # Elegimos un carácter al azar de nuestra lista y lo añadimos a 'password'
    password.append(random.choice(caracteres))

# Mezclamos la lista de la contraseña final para mayor seguridad
random.shuffle(password)

# Convertimos la lista de caracteres en un solo texto (string) y lo imprimimos
print("Tu nueva contraseña es:", "".join(password))
'''
