## Ejercicio 1



## Ejercicio 1
class BasicStats2():

    def __init__(self, listaDeValores, getStats = True):
        """Constructor"""

        self.listaDeValores = listaDeValores

        if getStats:
            self.media = self.getMedia(self.listaDeValores)
            self.var = self.getVar(self.listaDeValores)
            self.sdv = self.getSDv(self.listaDeValores)

    @classmethod
    def getMedia(cls, lista):
        """Calcula la media"""
        return sum(lista)/len(lista)

    @classmethod
    def getVar(cls, lista):
        """Calculo la varianza"""

        media = cls.getMedia(lista)
        return sum([(i-media)**2 for i in lista])/len(lista)

    @classmethod
    def getSDv(cls, lista):
        """Calculo la varianza"""

        media = cls.getMedia(lista)
        return cls.getVar(lista)**(1/2)

lista2 = [4,23,4,5,6,90,23,45,67]
grupoControl2 = BasicStats2(lista2)
print(grupoControl2.media)
print(grupoControl2.sdv)

lista3 = [1,2,3,4,5,6,7,9,10]
BasicStats2.getSDv(lista3)


