"""Programa que pida dos números al usuario y una operación matemática a ejecutar con esos dos números.
Las operaciones son:
-> Suma
-> Resta (al primero menos el segundo)
-> Multiplicación
-> División (al primero sobre el segundo)
-> Exponenciación (el primero es la base y el segundo el exponente)
-> Radicación (el primero es el radicando y el segundo es el índice)"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def exponenciacion(a, b):
    return a ** b

def radicacion(a, b):
    return a ** (1/b)

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Exponenciación")
print("6. Radicación")
opc = int(input("Ingrese la opción que desea: "))

if opc == 1:
    print(n1, "+", n2, "=", suma(n1, n2))
elif opc == 2:
    print(n1, "-", n2, "=", resta(n1, n2))
elif opc == 3:
    print(n1, "*", n2, "=", multiplicacion(n1, n2))
elif opc == 4:
    print(n1, "/", n2, "=", division(n1, n2))
elif opc == 5:
    print(n1, "^", n2, "=", exponenciacion(n1, n2))
elif opc == 6:
    print(n1, "^ 1/", n2, "=", radicacion(n1, n2))
else:
    print("ERROR: Ingrese un número válido.")
