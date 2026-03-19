
mi_lista= [3,3,5,1,4,5,3,1,1,4,5,7,8,2,3]
mi_lista_aux= []

for elemento in mi_lista:
    if elemento not in mi_lista_aux:
        mi_lista_aux.append(elemento)
        
print("la lista inicial es:", mi_lista)
print("la lista sin duplicado es:", mi_lista_aux)

'''
otras maneras de resolver esto:

El camino rápido: Usando set() 
Un set (conjunto) es una estructura de datos que, por definición, no permite elementos duplicados.

mi_lista = [3, 3, 5, 1, 4, 5, 3, 1, 1, 4, 5, 7, 8, 2, 3]
resultado = list(set(mi_lista))

print(resultado)
----------------

Manteniendo el orden: Usando dict.fromkeys()
Si necesitas eliminar los duplicados pero mantener el orden en que aparecieron los elementos por primera vez, esta es la mejor opción.
mi_lista = [3, 3, 5, 1, 4, 5, 3, 1, 1, 4, 5, 7, 8, 2, 3]

resultado = list(dict.fromkeys(mi_lista))

print(resultado)
-----------

3. El estilo funcional: List Comprehension
Aunque no es la más eficiente, es elegante para scripts rápidos:


mi_lista = [3, 3, 5, 1, 4, 5, 3, 1, 1, 4, 5, 7, 8, 2, 3]
vistos = set()
resultado = [x for x in mi_lista if not (x in vistos or vistos.add(x))]

print(resultado)
------------

'''
