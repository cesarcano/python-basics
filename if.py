edad = int(input("¿Cuantos años tienes? "))
if edad <= 4:
    precio = 0
elif edad <= 18:
    precio = 70
else:
    precio = 140
print("El precio de la entrada es", "$" ,precio)