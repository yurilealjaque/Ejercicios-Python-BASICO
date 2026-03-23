'''
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 
 
 ¿Cómo funciona técnicamente?

El cifrado se puede ver como una operación matemática:

C=(P+K)mod n

Donde:

P = posición de la letra original
k = número de desplazamientos (clave)
n = tamaño del alfabeto (26 o 27 en español)
C = letra cifrada

¿Cómo se descifra?

P=(C-k)mod n

'''

import string

def cifrado_cesar(text, decrypt= False, shift = 3):
    alphabet = list(string.ascii_lowercase) # string.ascii_lowercase: Nos da la cadena "abcdefghijklmnopqrstuvwxyz". list convierte la cadena resultante en una lista
    alphabet.insert(alphabet.index("n") +1, "ñ") # aca se inserta la ñ(no esta en la legua inglesa) , se busca la posicion de "n", a esta posicion se le suma 1 y gracias a la funcion insert se agrega la "ñ"(27 letras ahora tiene el alfabeto)
    
    cesar_text = ""
    
    for value in text.lower():  #text.lower(): Convertimos todo a minúsculas
        if value in alphabet:   #Si el carácter es una letra (y no un espacio o un punto), entramos a procesarlo.
            index = (alphabet.index(value)+ (-shift if decrypt else shift)) % len(alphabet) #alphabet.index(value): Buscamos la posición actual de la letra (ej. 'a' es 0).
            #(-shift if decrypt else shift): Esto es un operador ternario. Si decrypt es verdadero, el número se vuelve negativo (retrocedemos); si es falso, queda positivo (avanzamos).
            
            cesar_text+= alphabet[index]
        else:
            cesar_text += value
            
    print(cesar_text)
    
cifrado_cesar("mi nombre es yuri leal jaque")
cifrado_cesar("ol proeuh hv bxul ñhdñ mdtxh", True)

#% len(alphabet): El operador Módulo. Es la magia que hace que el abecedario sea "circular". 
#Si llegas a la 'z' (posición 26) y sumas 1, te daría 27 (fuera de rango). Pero 27 % 27 es 0, lo que te devuelve al inicio ('a').
#cesar_text += ...: Buscamos la letra en la nueva posición y la pegamos al resultado.


