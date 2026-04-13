"""programa que calcule la tabla de multiplicacion de cualquier numero entero dado por el usuario
debe calcular la tabla de 0 hasta el 12""" 


def tabla_multiplicar(n1, n2):
    return str(n1)+ "*"+ str(n2)+ "="+ str(n1*n2)

n= int(input("ingrese el numero entero: "))

for i in range(0,13):
    print(tabla_multiplicar(n,i))