"""Programa que valide si una contraseña especificada por el usuario es segura.
Una contraseña segura:
-> Tiene más de 8 caracteres
-> Tiene al menos una letra mayúscula
-> Tiene al menos un número
-> No debe tener espacios
"""


#print(len("Hola")) #cuenta la cadena
#print("a".isupper()) #verifica si hay alguna letra mayuscula
#print("a".isnumeric()) #verifica si hay un numero

def contraseña(password):
    largo = False
    mayus = False
    numer= False
    espacio = False
    if len(password) > 8:
        largo = True
    
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True
        if password[i].strip():
            espacio= True
            
    if largo and mayus and numer and espacio:
        return True
    else:
        return False
    
password= input ("ingrese una contraseña: ")
verificacion= contraseña(password)
if verificacion:
    print("la contraseña es segura")
else:
    print("la contraseña no es segura")
