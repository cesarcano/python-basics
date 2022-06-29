from mailbox import NoSuchMailboxError


class alumno:

    def __init__(self):
        self.nombre = input("cual es tu nombre")
        self.nota = input("cual es tu calificaicon final")
    
    def imprimir(self):
        print("nombre del alumno", self.nombre)
        print
        ("nota", self.nota)

    def resultado (self):
        if int(self.nota) <7:
            print ("El alumno reprobo")
        else:
            print("El alumno aprobo")

alumno1 = alumno()

alumno1.imprimir()
alumno1.resultado()