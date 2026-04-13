

def salarioTrabajador(salario, x):
    nuevoSalario= salario + (salario*(x/100)) 
    return nuevoSalario


salarioActual = float(input("ingrese el salario actual del trabajador: "))
incremento= float(input("ingrese el porcentaje de incremento que tendra el salario del trabajador: "))

nuevoSalario = salarioTrabajador(salarioActual, incremento)

print (f"el nuevo salario del trabajador es: {nuevoSalario}")