
class UnidadCurricular():
    """Esta clase esta dedicada a generar las unidades curriculares y asignar previas, etc"""
    def __init__(self,nombreUC:str, semestreUC:int, creditosUC:int , Codigo:str):
        """Constructor"""
        self.nombre = nombreUC
        self.semestre = semestreUC
        self.credit = creditosUC
        self.codigo= Codigo

    def mostrar_creditos(self):
        return self.credit

    def mostrar_nombre(self):
        return self.nombre
    def mostrar_semestre(self):
        return self.semestre
    
    def generar_codigo(self): 
        return self.codigo

    def mostrar_datos(self):
        datosuc= {"UC":self.nombre, "creditos": self.credit, "codigo": self.codigo}
        return datosuc


class Plan_Estudio(UnidadCurricular):
    """Esta clase toma la las UCs y las guarda en un documento txt ordenada por semestre"""
    def __init__(self,nombreUC:str, semestreUC:int, creditosUC:int , Codigo:str, Previas:list = None, Aprobadas:list = None):
        super().__init__(nombreUC, semestreUC, creditosUC, Codigo)
        if semestreUC == 1:
            self.nombre= nombreUC
            self.credit = creditosUC
            self.codigo = Codigo
            self.semestre=semestreUC
        elif semestreUC == 2:
            if Previas == None:
               raise ValueError("Ingrese las Previas de la UC")
            else:
                self.nombre = nombreUC
                self.previa = Previas
                self.semestre = semestreUC
                self.credit = creditosUC
                self.codigo= Codigo
        else:
            if Previas== None and Aprobadas == None:
                raise ValueError("Ingrese las Previas de la UC y las Aprobadas de la UC") 
            else:
                self.nombre = nombreUC
                self.previa = Previas
                self.semestre = semestreUC
                self.aprob = Aprobadas
                self.credit = creditosUC
                self.codigo= Codigo
                
    def ordenar_por_semestre(self):
        """"""
        if self.mostrar_semestre() == 1:
            texto= open("Uc\S1.txt", "a")
            texto.write(f"\n{str(self.mostrar_datos())}")
            texto.close()
            return f"UC guardada en S1 con codigo {self.generar_codigo()}"
        elif self.mostrar_semestre() == 2:
            texto= open("Uc\S2.txt", "a")
            texto.write(f"{str(self.mostrar_datos())}, Previas: {self.mostrar_previas()}\n")
            texto.close()
            return f"UC guardada en S2 con codigo {self.generar_codigo()}"
        elif self.mostrar_semestre() == 3:
            texto= open("Uc\S3.txt", "a")
            texto.write(f"{str(self.mostrar_datos())}, Previas: {str(self.mostrar_previas())}, Aprobadas: {str(self.mostrar_aprob())}\n")
            texto.close()
            return f"UC guardada en S3 con codigo {self.generar_codigo()}"
        elif self.mostrar_semestre() == 4:
            texto= open("Uc\S4.txt", "a")
            texto.write(f"{str(self.mostrar_datos())}, Previas: {str(self.mostrar_previas())}, Aprobadas: {str(self.mostrar_aprob())}\n")
            texto.close()
            return f"UC guardada en S4 con codigo {self.generar_codigo()}"
        elif self.mostrar_semestre() == 5:
            texto= open("Uc\S5.txt", "a")
            texto.write(f"{str(self.mostrar_datos())}, Previas: {str(self.mostrar_previas())}, Aprobadas: {str(self.mostrar_aprob())}\n")
            texto.close()
            return f"UC guardada en S5 con codigo {self.generar_codigo()}"
        elif self.mostrar_semestre() == 6:
            texto= open("Uc\S6.txt", "a")
            texto.write(f"{str(self.mostrar_datos())}, Previas: {str(self.mostrar_previas())}, Aprobadas: {str(self.mostrar_aprob())}\n")
            texto.close()
            return f"UC guardada en S6 con codigo {self.generar_codigo()}"

    def mostrar_aprob(self):
        if self.semestre == 1:
            return "no tiene aprobadas"
        return self.aprob

    def mostrar_previas(self):
        if self.semestre == 1:
            return "no tiene previas"
        else:
            return self.previa

  
