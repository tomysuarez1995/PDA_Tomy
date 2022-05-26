from debugpy import listen
from Rol import Ingreso
from Plan_de_Estudio import UnidadCurricular, Plan_Estudio

class Matriculacion():
    """Esta clase administra todo"""
    def __init__(self,ingresar:str= None,cedula:int=None, matricularuc=None, desmatricularuc=None,matricularex=None, desmatricularex=None, leerlistaEx=None, leerlistaUc=None, veraprob=None, verprev=None):
        """"""
        if ingresar == "E" or ingresar== "e":
            if cedula == None:
                raise ValueError("ingrese su cedula de Estudiante")
            else:
                self.matrUC= matricularuc
                self.matrEX= matricularex
                self.verap= veraprob
                self.verpr= verprev
                rol = open("rol.txt", "r")
                for linea in rol:
                    if linea.split()[8]== "3":
                        if linea.split()[4]==str(cedula):
                            list1=linea.split()[1::2]
                            list2=linea.split()[::2]
                            list2.pop(0)
                            diccest= dict(zip(list1, list2))
                            del diccest["rol"]
                            print(f"se ingreso como Estudiante con los datos \n{diccest}")
        elif ingresar == "a" or ingresar =="A":
                self.matrUC= matricularuc
                self.matrEX= matricularex
                self.desmUC= desmatricularuc
                self.desmEX= desmatricularex
                self.leerUC= leerlistaUc
                self.leerEX= leerlistaEx
                rol = open("rol.txt", "r")
                for linea in rol:
                    if linea.split()[8]=="1":
                        list1= linea.split()[1::2]
                        list2=linea.split()[::2]
                        list2.pop(0)
                        diccadm = dict(zip(list1, list2))
                        del diccadm["rol"]
                        print(f"se ingreso como Administrador con los datos \n{diccadm}")
        elif ingresar == "C" or ingresar =="c":
                self.leerUC= leerlistaUc
                self.leerEX= leerlistaEx
                rol = open("rol.txt", "r")
                for linea in rol:
                    if linea.split()[8]=="2":
                        list1= linea.split()[1::2]
                        list2=linea.split()[::2]
                        list2.pop(0)
                        diccoord = dict(zip(list1, list2))
                        del diccoord["rol"]
                        print(f"se ingreso como Coordinador/a con los datos \n{diccoord}")

    # def existencia(self):
    #     rol = open("rol.txt", "r")
    #     for linea in rol:
    #         if self.ingr == "C" or self.ingr == "c":
    #             if linea.split()[8]=="2":
    #                 list1= linea.split()[1::2]
    #                 list2=linea.split()[::2]
    #                 list2.pop(0)
    #                 diccoord = dict(zip(list1, list2))
    #                 del diccest["rol"]
    #                 return f"se ingreso como Administrador con los datos \n{diccoord}"
    #         elif self.ingr == "E" or self.ingr == "e":
    #             if linea.split()[8]=="3":
    #                 listEstud = []
    #                 list1= linea.split()[1::2]
    #                 list2=linea.split()[::2]
    #                 list2.pop(0)
    #                 diccest= dict(zip(list1, list2))
    #                 del diccest["rol"]
    #                 listEstud.append(diccest)
    #                 return f"se ingreso como Administrador con los datos \n{diccest}"
    #         elif self.ingr == "A" or self.ingr == "a":
    #             if linea.split()[8]=="1":
    #                 list1= linea.split()[1::2]
    #                 list2=linea.split()[::2]
    #                 list2.pop(0)
    #                 diccadm = dict(zip(list1, list2))
    #                 del diccest["rol"]
    #                 return f"se ingreso como Administrador con los datos \n{diccadm}"
    #     rol.close()

    def Administrador(self):
        """La funcion secretaria nos devuelve el poder desmatricular, el matricular y ver listas"""
    
    def Coordinadora(self):
        """clase coordinadora, permisos de leer lista examen y lista de UC"""
        
        
    def Estudiante():
        """clase Estudiante, solo puede matricularse y leer aprobadas y matriculadas al igual que examenes"""
        
    

    

