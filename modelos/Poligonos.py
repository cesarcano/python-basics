from re import L
from modelos.Figurasgeometricas import Figurasgeometricas

class poligonos(Figurasgeometricas):
    def __init__(self,per,apot,l1,l2,l3,l4,l5):
        self.perimetro=per
        self.apotema=apot
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3
        self.lado4=l4
        self.lado5=l5

    def calcularArea(self):
        return (self.perimetro * self.apotema)/2

    def calculaPerimetro(self):
        return ((self.lado1)+(self.lado2)+(self.lado3)+(self.lado4)+(self.lado5))
        
    