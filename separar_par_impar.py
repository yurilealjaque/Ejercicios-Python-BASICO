def separar_pares_impares(lista_entrada):
    
    lista_pares, lista_impares= [], []
    
    for numero in lista_entrada:
        #caso de que el numero es par:
        if numero % 2 == 0:
            lista_pares.apped(numero)
            
        #caso de que el numero es ipar:
        else:
            lista_impares.append(numero)
            
    return lista_pares, lista_impares

mi_lista = [2,3,3,8,1,20,5,14,22,21,31,84,15,26,9]

print("la lista inicial es ", mi_lista)

lista_pares, lista_impares = separar_pares_impares(mi_lista)

print("la sublista de numeros pares es ", lista_pares)
print("la sublista de numeros pares es ", lista_impares)