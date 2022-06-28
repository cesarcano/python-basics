# Crear un programa que me pregunte mi edad y me diga lo siguiente;
# 1. Si soy mayor de edad
# 2. Cuanto me falta para mi retiro (65 años)
# 3. En que año nací suponiendo que estamos en el 2022
# Utilizar funciones (def) 

def esMayordeEdad(age):
    if age < 18:
        print("Eres menor de edad")
    else:
        print ("Eres mayor de edad")

def retirementAge(e):
    print ("te faltan",65-e,"años para retirarte")

def yearBorn(n):
    print ("naciste en",2022-n)

nombre = str(input("¿Cual es tu nombre?"))
edad =int(input("¿Cuantos años tienes? "))

esMayordeEdad(edad)
retirementAge(edad)
yearBorn(edad)
