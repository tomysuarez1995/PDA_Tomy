## Ejercicio 1
class BasicStats():

    def __init__(self, listaDeValores):
        """Constructor"""
        self.listaDeValores = listaDeValores

    def getMedia(self):
        """Calcula la media"""

        return sum(self.listaDeValores)/len(self.listaDeValores)


    def getVar(self):
        """Calculo la varianza"""

        media = self.getMedia()
        return sum([(i-media)**2 for i in self.listaDeValores])/len(self.listaDeValores)


    def getSDv(self):
        """Calculo la varianza"""

        media = self.getMedia()
        return (sum([(i-media)**2 for i in self.listaDeValores])/len(self.listaDeValores))**(1/2)

            

lista = [1,2,3,4,5,10,2,33,4]

grupoControl = BasicStats(lista)
print(grupoControl.getMedia())
print(grupoControl.getVar())
print(grupoControl.getSDv())


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
