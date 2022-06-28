# Crear un programa que reciba N numero de nombres y los ordene alfabéticamente
# Utilizar Listas y funciones

listName=[]
print ("cuantos nombres son")
total= int(input())
i = 0
while i < total:
    print ("ingrese el nombre", i+1)
    name = str(input())
    listName.append(name)
    i += 1
listName.sort()

print (listName)







