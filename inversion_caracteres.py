
cadena = "Python"

cadena_resultado= ""

contador =1
while contador <= len(cadena):
    
    cadena_resultado = cadena_resultado + cadena[-contador]
    
    contador += 1
    
print("cadena original: " + cadena)
print("cadena resultado: " + cadena_resultado)

'''
cadena = "Python"

cadena_resultado= ""

contador =1
while contador <= 0:
    
    cadena_resultado = cadena_resultado + cadena[-contador]
    
    contador -= 1
    
print("cadena original: " + cadena)
print("cadena resultado: " + cadena_resultado)

-------- utilizando indices-------


cadena = "Python"

cadena_resultados = cadena[-1:-len(cadena)-1:-1]

print(cadena_resultado)






'''
