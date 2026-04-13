"""Programa que convierta una unidad en dias, horas, minutos y segundos a segundos"""

"""def calcularSegundos(dias, horas, minutos, segundos):
    segundosTotales = 0
    segundosTotales += segundos
    segundosTotales += minutos * 60
    segundosTotales += horas * 60 * 60
    segundosTotales += dias * 24 * 60 * 60
    return segundosTotales

dias = int(input("Ingrese la cantidad de dias: "))
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

segundosTotales = calcularSegundos(dias, horas, minutos, segundos)

print("La cantidad de segundos en el tiempo ingresado es de:", segundosTotales)"""

"---------------------------------------------------------"

def calcular_segundos(dias, horas, minutos, segundos):
    return segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)

dias = int(input("Días: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total = calcular_segundos(dias, horas, minutos, segundos)
print(f"Total de segundos: {total}") 