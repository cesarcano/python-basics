from mailbox import NoSuchMailboxError


class alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("nombre del alumno", self.nombre)
        print("nota", self.nota)

    def resultado (self):
        if self.nota <7:
            print ("el alumno reprobo")
        else:
            print("el alumno aprobo")

alumno1 = alumno("diego",4)
alumno2 = alumno("saul",10)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()


     