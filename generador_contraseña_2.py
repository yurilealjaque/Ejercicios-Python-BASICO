import random, string

caracteres = list(string.ascii_letters + string.digits + "!#@%&*")

letras = list(string.ascii_letters)
numeros = list(string.digits)
especiales = list("!#@%&*")

tam = int(input("Por favor, introduce un tamaño para la contraseña: "))

if tam < 6 or tam > 16:
    print("Error! Introduce un tamaño entre 6 y 16 caracteres.")
else:
    random.shuffle(caracteres)
    
    password = []
    
    password.append(random.choice(letras))
    password.append(random.choice(numeros))
    password.append(random.choice(especiales))
    
    for i in range(tam-3):
        password.append(random.choice(caracteres))
        
    random.shuffle(password)
    
    print("".join(password))




'''
import random, string

# 1. Preparamos las "bolsas" de ingredientes
caracteres = list(string.ascii_letters + string.digits + "!#@%&*") # Bolsa completa
letras = list(string.ascii_letters)  # Solo letras
numeros = list(string.digits)        # Solo números
especiales = list("!#@%&*")         # Solo símbolos

# 2. Entrada del usuario
tam = int(input("Por favor, introduce un tamaño para la contraseña: "))

# 3. Validación de rango (mínimo 6, máximo 16)
if tam < 6 or tam > 16:
    print("Error! Introduce un tamaño entre 6 y 16 caracteres.")
else:
    # Mezclamos la bolsa maestra
    random.shuffle(caracteres)
    
    password = [] # Lista para armar la contraseña
    
    # 4. ASEGURAMOS VARIEDAD: Agregamos uno de cada tipo obligatoriamente
    password.append(random.choice(letras))     # Agrega 1 letra
    password.append(random.choice(numeros))    # Agrega 1 número
    password.append(random.choice(especiales)) # Agrega 1 símbolo
    
    # 5. COMPLETAMOS EL RESTO:
    # Como ya agregamos 3, el ciclo corre hasta completar el tamaño pedido (tam - 3)
    for i in range(tam - 3):
        password.append(random.choice(caracteres))
        
    # 6. DESORDENAMOS TODO: 
    # Para que el orden Letra-Número-Símbolo no sea predecible
    random.shuffle(password)
    
    # 7. RESULTADO: Unimos la lista en un solo texto
    print("Contraseña generada:", "".join(password))


'''
