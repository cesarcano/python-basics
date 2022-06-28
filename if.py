# Crear un programa que me pregunte mi edad y me diga lo siguiente;
# 1. Si soy mayor de edad
# 2. Cuanto me falta para mi retiro (65 años)
# 3. En que año nací suponiendo que estamos en el 2022
# Utilizar funciones (def) 

edad = int(input("¿Cuantos años tienes? "))
if edad <= 4:
    precio = 0
elif edad <= 18:
    precio = 70
else:
    precio = 140
print("El precio de la entrada es", "$" ,precio)