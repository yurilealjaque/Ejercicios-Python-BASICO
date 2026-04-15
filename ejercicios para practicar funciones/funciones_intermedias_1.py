"""
-Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
-Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
-En ciudades, cambia “Cancún” por “Monterrey”
-En las coordenadas, cambia el valor de “latitud” por 9.9355431"""

matriz = [[10, 15, 20], [3, 7, 14]]


matriz[1][0] = 6  # se accede a la fila 1, columna 0

print(matriz) # resultado: [[10, 15, 20], [6, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]


cantantes[0]["nombre"] = "Enrique Martin Morales" # El primer cantante es el índice 0 de la lista

print(cantantes[0]["nombre"]) # resultado: Enrique Martin Morales

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}


ciudades["México"][2] = "Monterrey"  # Accedemos a la llave 'México' y luego al índice 2 de su lista

print(ciudades["México"]) # resultado: ['Ciudad de México', 'Guadalajara', 'Monterrey']
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]


coordenadas[0]["latitud"] = 9.9355431 # Accedemos al primer elemento de la lista (el diccionario) y cambiamos la latitud

print(coordenadas[0]["latitud"]) # resultado: 9.9355431

"""_______________________________________________________________________________________"""

def iterarDiccionario(lista):# primero recorremos cada diccionario dentro de la lista
    
    for diccionario in lista: # se crea una lista temporal para guardar cada par "llave - valor"
        
        linea = []
        for llave, valor in diccionario.items():
            linea.append(f"{llave} - {valor}")
        
        
        print(", ".join(linea))  # Unimos los elementos de la lista con una coma y un espacio

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

"""_____________________________________________________________________________"""

def iterarDiccionario2(llave, lista):
    
    for diccionario in lista: # Recorremos cada diccionario en la lista
        
        if llave in diccionario: # Verificamos si la llave existe en el diccionario actual
            print(diccionario[llave])
        else:
            print(f"La llave '{llave}' no se encontró en este registro.")


cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("Valores de 'nombre':")
iterarDiccionario2("nombre", cantantes)

print("\nValores de 'pais':")
iterarDiccionario2("pais", cantantes)

"""_________________________________________________________________________________"""

def imprimirInformacion(diccionario):
    
    for llave, lista in diccionario.items(): # se itera por cada llave y su lista correspondiente
        
        print(f"{len(lista)} {llave.upper()}") # se imprime la longitud de la lista y la llave en mayúsculas
        
        
        for item in lista: # se itera por la lista para imprimir cada valor
            print(item)
        
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)