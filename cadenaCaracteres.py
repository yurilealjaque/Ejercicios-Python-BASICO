cadena = input("Por favor, introduce una cadena de caracteres: ")

# --- Solución básica ---

pares = ""    # Cambiamos el nombre: aquí van los índices 0, 2, 4...
impares = ""  # Aquí van los índices 1, 3, 5...

contador = 0
while contador < len(cadena):  # recordar que la cadena parte en 0 osea si pongo la palabra python tiene un largo de 6 (lo que ve len) sin eenvargo en la lista parte de 0 , osea seria 5 elementos , por ende si ocupo el =< buscaria el elemento 6 que no existe en la lista por ende eso seria un error
    # Si el índice es par (0, 2, 4...)
    if contador % 2 == 0:
        pares = pares + cadena[contador]
    # Si el índice es impar (1, 3, 5...)
    else:
        impares = impares + cadena[contador]

    contador += 1

# --- Solución avanzada (Slicing) ---

# [inicio : fin : salto]
pares2 = cadena[::2]    # Empieza en 0 y salta de 2 en 2
impares2 = cadena[1::2] # Empieza en 1 y salta de 2 en 2

print("Cadena original: " + cadena)
print("Caracteres en posiciones PARES (0, 2, 4): " + pares)
print("Caracteres en posiciones IMPARES (1, 3, 5): " + impares)


'''cadena = input("Por favor, introduce una cadena de caracteres: ")

# --- SOLUCIÓN BÁSICA (Manual) ---

pares = ""
impares = ""
contador = 0

# Recorremos la palabra letra por letra
while contador < len(cadena):
    # ¿El índice actual es divisible por 2?
    if contador % 2 == 0:
        # Si el índice es 0, 2, 4... se guarda aquí
        impares = impares + cadena[contador]
    else:
        # Si el índice es 1, 3, 5... se guarda aquí
        pares = pares + cadena[contador]

    contador += 1 # Avanzamos a la siguiente posición

# --- SOLUCIÓN AVANZADA (Slicing) ---

# Toma desde el inicio (0), saltando de 2 en 2
impares2 = cadena[::2] 

# Toma desde el índice 1, saltando de 2 en 2
pares2 = cadena[1::2] 

print("Cadena original: " + cadena)
print("Índices pares (0,2,4): " + impares)
print("Índices impares (1,3,5): " + pares)





1. El desfase del número 0
Recuerda que Python empieza a contar en 0. Si una palabra tiene 6 letras (como "PYTHON"), sus índices son: 0, 1, 2, 3, 4, 5.

El largo (len) de la cadena es 6.

Pero no existe el índice 6.

2. ¿Qué pasaría con <=?
Si usas while contador <= len(cadena):

El robot llega al índice 5 (la última letra, la 'N'), hace su trabajo y suma 1 al contador.

Ahora el contador vale 6.

Como 6 es igual a 6 (el largo de la cadena), el while intenta dar una vuelta más.

El código intenta buscar cadena[6].

¡BUM! Python busca una letra que no existe y el programa se detiene con un error.

'''
