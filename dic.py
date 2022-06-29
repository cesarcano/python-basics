from typing import Dict


listCar = []

def createCar() : 
    auto = {}
    auto["marca"] = input("¿Que marca es tu vehiculo?")   
    auto["año"] = (input("¿Que año es tu vehiculo?"))
    auto["modelo"] = (input("¿Que modelo es tu vehiculo?"))
    auto["color"] = (input("¿Que color es tu vehiculo?"))
    print (auto)
    listCar.append(auto)

def main():
    respuesta = "si"
    
    while respuesta == "si":
        createCar()
        respuesta = input("¿desea agregar un nuevo vehiculo?")
    
    print(listCar)

    
main()




