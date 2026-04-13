def calcular_suma(*numeros):  #*args empaqueta todo en una tupla
    
    return sum(numeros) # sum() suma todos los elementos de una colección

def calcular_resta(*numeros):
    if not numeros: # esto declara "si NO es verdad" o "si está vacío"
        return 0
    
    resultado = numeros[0] # Iniciamos con el primer número de la lista
    
    for siguiente_numero in numeros[1:]: #es un slicing. Significa: "toma desde la posición 1 hasta el final".
        resultado -= siguiente_numero  # En cada vuelta del ciclo, le quitamos el número actual al total.
    return resultado

def calcular_multiplicacion(*numeros):
    if not numeros: 
        return 0
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

def calcular_division(*numeros):
    if not numeros: 
        return 0
    resultado = numeros[0]
    for divisor in numeros[1:]:
        if divisor == 0:
            return "Error: No se puede dividir por cero"
        resultado /= divisor
    return resultado

def calcular_exponenciacion(*numeros):
    if not numeros: 
        return 0
    resultado = numeros[0]
    for exponente in numeros[1:]:
        resultado **= exponente
    return resultado

def calcular_radicacion(*numeros):
    if not numeros: 
        return 0
    resultado = numeros[0]
    for indice_raiz in numeros[1:]:
        if indice_raiz == 0:
            return "Error: El índice de la raíz no puede ser cero"
        resultado **= (1 / indice_raiz)
    return resultado

# --- Flujo del Programa ---

print("--- Calculadora de Parámetros Ilimitados ---")
entrada_usuario = input("Ingrese los números que desee, separados por un espacio: ")

try:
    # Transformamos el texto ingresado en una lista de números reales (float)
    lista_de_numeros = [float(texto) for texto in entrada_usuario.split()] # Si el usuario escribe "10 20 30", esta función lo corta por los espacios y crea una lista de textos: ["10", "20", "30"].
    
    if len(lista_de_numeros) < 1:
        print("Error: No ingresó ningún número para operar.")
    else:
        print("\nMenú de Operaciones:")
        print("1. Sumar todos")
        print("2. Restar (el primero menos los demás)")
        print("3. Multiplicar todos")
        print("4. Dividir (el primero entre los demás)")
        print("5. Potencia consecutiva")
        print("6. Raíz consecutiva")
        
        opcion_elegida = int(input("\nSeleccione el número de la operación: "))

        # Usamos el asterisco (*) para "desempaquetar" la lista y pasarla a los *args
        if opcion_elegida == 1:
            print(f"Resultado: {calcular_suma(*lista_de_numeros)}")
        elif opcion_elegida == 2:
            print(f"Resultado: {calcular_resta(*lista_de_numeros)}")
        elif opcion_elegida == 3:
            print(f"Resultado: {calcular_multiplicacion(*lista_de_numeros)}")
        elif opcion_elegida == 4:
            print(f"Resultado: {calcular_division(*lista_de_numeros)}")
        elif opcion_elegida == 5:
            print(f"Resultado: {calcular_exponenciacion(*lista_de_numeros)}")
        elif opcion_elegida == 6:
            print(f"Resultado: {calcular_radicacion(*lista_de_numeros)}")
        else:
            print("ERROR: La opción seleccionada no existe.")

except ValueError:
    print("ERROR: Ingrese solo valores numéricos válidos.")