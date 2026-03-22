'''1. Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.

'''
def custom_max(n1,n2):
    """Dado 2 numeros de entrada retorna el maximo de ambos

    Args:
        n1 (_int_): Primer numero a comparar
        n2 (_int_): Segundo numero a comparar

    Returns:
        int : mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1==n2:
        raise Exception("los valores no pueden ser iguales")
    raise Exception("Algo salio mal")
    
print(custom_max(1,2))

'''
Los docstrings en Python se crean colocando una cadena de texto (string) entre comillas triples (""" """ o ''' ''') 
justo debajo de la definición de una función, clase o módulo. Sirven para documentar qué hace el código, sus parámetros y lo que devuelve, 
y se puede acceder a ellos usando help() o el atributo __doc__. 

'''

'''1. Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
solucion: 
a>b>c
b>c
a>c

'''

def max_de_tres(n1,n2,n3):
    
    n= custom_max (n1,n2)
    n_final= custom_max(n3,n)
    
    return n_final
        
