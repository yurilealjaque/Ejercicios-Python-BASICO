'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

def fizz_buzz():
    for numero in range(1,101):
        if numero % 3== 0 and numero % 5 == 0: #IMPORTANTE!!! Si pusiéramos la condición de fizz (múltiplo de 3) al principio, el programa entraría ahí primero para el número 15, imprimiría "fizz" y saltaría al siguiente número, perdiendo la oportunidad de imprimir "fizzbuzz"
            print("fizzbuzz")
        elif numero % 3== 0 :
            print("fizz")
        elif numero % 5==0 :
            print("buzz")
        else:
            print(numero)

fizz_buzz()

'''
OTRA MANERA DE HACER ESTE EJERCICIO:


numero = ''

for i in range(1, 101):
    if (i % 3 == 0):
        numero = 'fizzbuzz' if i % 5 == 0 else 'fizz' # "Guarda 'fizzbuzz' si también es divisible por 5; de lo contrario, guarda solo 'fizz'". Es una forma muy compacta de resolver el problema del 15 (el múltiplo de ambos).
    elif (i % 5 == 0):
        numero = 'buzz'
    else:
        numero = i
        
    print(numero)
    
'''