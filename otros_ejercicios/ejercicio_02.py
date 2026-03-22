'''
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''
def es_vocal(caracter):
 
    vocales = "aeiou"
    return caracter.lower() in vocales

print(es_vocal('a'))  
print(es_vocal('E'))  
print(es_vocal('z'))  