class fraccion:

    def __init__(self,num,den):
        self.num = num
        self.den = den

    def imprime(self):
        print("{",self.num,"/", self.den,"}")

def main():
    a = fraccion (5,7)
    a.imprime

    b = fraccion (3,2)
    b.imprime
main()
