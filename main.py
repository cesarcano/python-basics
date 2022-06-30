from modelos.Cuadrilateros import cuadrilateros
from modelos.Triangulos import triangulos
from modelos.Poligonos import poligonos


def main():
    cuadrado = cuadrilateros(10, 2)
    print ("cuadrado")
    print(cuadrado.calculaPerimetro()) 
    print(cuadrado.calcularArea())
    
def tria():
    triagulo = triangulos(10,10,3,3,3)
    print ("triangulo")
    print(triagulo.calcularArea())
    print(triagulo.calculaPerimetro())

def poli():
    poligono = poligonos(20,3,4,4,4,4,4)
    print ("poligono")
    print(poligono.calcularArea(),"cm2")
    print(poligono.calculaPerimetro())

main()
tria()
poli()

