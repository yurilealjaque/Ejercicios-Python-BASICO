cadena1= input("introduce una cadena de caracteres: ")
cadena2 = input("introduce otra cadena de caracteres: ")


mitad_cadena1 = int(len(cadena1)/2)

primera_mitad= cadena1[:mitad_cadena1]
segunda_mitad= cadena1[mitad_cadena1:]

resultado= primera_mitad + cadena2 + segunda_mitad

print("Resultado: " + resultado)