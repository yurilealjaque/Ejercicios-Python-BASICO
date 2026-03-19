def mcm(numero1, numero2):
    
    if numero1> numero2:
        num_mayor = numero1
    else:
        num_mayor = numero2
        
    while(num_mayor % numero1) != 0 or (num_mayor % numero2) != 0:
        num_mayor += 1
        
    return num_mayor
 
print (mcm(20,6))