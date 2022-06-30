from re import L
from modelos.Figurasgeometricas import Figurasgeometricas

class triangulos(Figurasgeometricas):
    
    def __init__(self, ancho, alto, l1, l2,l3):
        self.altura = alto
        self.ancho = ancho
        self.lado1= l1
        self.lado2=l2
        self.lado3=l3
    
    
    # Sobrescribir metodo de clalculo de area
    def calcularArea(self):
        return (self.altura * self.ancho)/2

    def calculaPerimetro(self):
        return ((self.lado1)+(self.lado2)+(self.lado3))
        