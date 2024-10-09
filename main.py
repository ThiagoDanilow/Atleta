from Atletas import *

if __name__ == "__main__":

    c1 = Corredor("Bolt", 35, 90.5)
    n1 = Nadador("Cesar Cielo", 42, 85.5)
    ciclista1 = Ciclista("Henrique Avancini", 37, 75.0)

    print(c1)
    print(c1.aquecer())
    print(c1.correr())
    print(n1)
    print(n1.aquecer())
    print(n1.nadar())
    print(ciclista1)
    print(ciclista1.aquecer())
    print(ciclista1.pedalar())