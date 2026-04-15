# funciones_basicas_2.py

"""Crea las siguientes funciones

Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]
Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]
 

Crea el archivo un Python llamado funciones_basicas_2.py
Crea la función multiplica_por_dos(num)
Crea la función suma_y_resta(lista)
Crea la función sumatoria_menos_longitud(lista)
Crea la función valores_multiplicados_segundo(lista)
Crea la función valor_multiplicado_longitud(valor, longitud)"""


def multiplica_por_dos(num):
    """
    Crea una lista desde 0 hasta num, multiplicando cada entero por 2.
    Nota: En el ejemplo pusiste un 7, pero siguiendo la lógica de 
    multiplicar enteros por 2, los resultados siempre serán pares.
    """
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado

def suma_y_resta(lista):
    """
    Suma e imprime, resta y devuelve. 
    Asume que la lista tiene al menos 2 elementos.
    """
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)
    return resta

def sumatoria_menos_longitud(lista):
    """
    Suma todos los elementos y le resta la cantidad de elementos.
    """
    suma_total = sum(lista)
    return suma_total - len(lista)

def valores_multiplicados_segundo(lista):
    """
    Multiplica todos los elementos por el valor del índice 1.
    Maneja el error si la lista es muy corta.
    """
    if len(lista) < 2:
        print(len(lista))
        return []
    
    segundo_valor = lista[1]
    nueva_lista = []
    for valor in lista:
        nueva_lista.append(valor * segundo_valor)
    
    print(len(nueva_lista))
    return nueva_lista

def valor_multiplicado_longitud(valor, longitud):
    """
    Crea una lista de tamaño 'longitud' donde cada elemento 
    es 'valor * longitud'.
    """
    resultado = []
    valor_final = valor * longitud
    for i in range(longitud):
        resultado.append(valor_final)
    return resultado

# --- Pruebas (opcional para verificar) ---
# print(multiplica_por_dos(5))
# print(suma_y_resta([5, 4]))
# print(sumatoria_menos_longitud([1, 2, 3, 4]))
# print(valores_multiplicados_segundo([1, 3, 5, 7]))
# print(valor_multiplicado_longitud(7, 5))