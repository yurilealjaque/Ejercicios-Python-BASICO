

palabra = input("registra tu palbra: ")

palabra= palabra.lower()

l_palabra = list(palabra)

print(l_palabra)

l_palabra_reves = list(palabra)
l_palabra_reves.reverse()

while " " in l_palabra : #aca este while se ocupa para eliminar todos los espacios existentes de las palabras, el while hace un bucle para eliminar todos los espacios
    l_palabra.remove(" ")
    
while " " in l_palabra_reves: #aca este while se ocupa para eliminar todos los espacios existentes de las palabras, el while hace un bucle para eliminar todos los espacios
    l_palabra_reves.remove(" ")

if palabra == l_palabra_reves:
    print("esto es un palindromo")
else:
    print("esto no es un palindromo") 