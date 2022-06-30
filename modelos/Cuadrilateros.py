from re import L
from modelos.Figurasgeometricas import Figurasgeometricas

class cuadrilateros(Figurasgeometricas):
    
    def __init__(self, ancho, alto):
        self.altura = alto
        self.ancho = ancho
        
    # Sobrescribir metodo de clalculo de area
    def calcularArea(self):
        return self.altura * self.ancho

    def calculaPerimetro(self):
        return (self.altura + self.ancho) * 2


    # # SETTERS
    # def setAlto(self, value):
    #     self.altura = value

    # def setAncho(self, value):
    #     self.ancho = value

    # # GETTERS
    # def getAlto(self):
    #     return self.altura

    # def getAncho(self):
    #     return self.ancho