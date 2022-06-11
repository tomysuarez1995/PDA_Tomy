from Rol import Ingreso
from Plan_de_Estudio import UnidadCurricular, Plan_Estudio

class Matriculacion():
    """Esta clase administra todo"""
    def __init__(self,ingresar:str= None,cedula:int=None, matricularuc=None, desmatricularuc=None,matricularex=None, desmatricularex=None, leerlistaEx=None, leerlistaUc=None, veraprob=None, verprev=None):
        """"""
        print(f"bienvenido/a \n{self.usuario(ingresar, cedula)}")
    

    def usuario(self, ingresar, cedula):
        """define existencia de usuario"""
        if cedula==None:
            raise ValueError("ingrese una cedula para continuar")
        else:
            rol = open("rol.txt", "r")
            for linea in rol:
                if ingresar == "E" or ingresar== "e":
                    if linea.split()[8]== "3":
                        if linea.split()[4]==str(cedula):
                            list1=linea.split()[1::2]
                            list2=linea.split()[::2]
                            list2.pop(0)
                            diccest= dict(zip(list1, list2))
                            diccoord.pop("rol")
                            diccoord.pop("ingeso")
                            return diccest
                elif ingresar == "C" or ingresar =="c":
                        if linea.split()[8]=="2":
                            if linea.split()[4]==str(cedula):
                                list1= linea.split()[1::2]
                                list2=linea.split()[::2]
                                list2.pop(0)
                                diccoord = dict(zip(list1, list2))
                                diccoord.pop("rol")
                                diccoord.pop("ingeso")
                                return diccoord
                elif ingresar == "a" or ingresar =="A":
                        if linea.split()[8]=="1":
                            if linea.split()[4]==str(cedula):
                                list1= linea.split()[1::2]
                                list2=linea.split()[::2]
                                list2.pop(0)
                                diccadm = dict(zip(list1, list2))
                                diccoord.pop("rol")
                                diccoord.pop("ingeso")
                                return diccadm
    

        


class Administrador(Matriculacion):
    def __init__(self,ingresar:str= None,cedula:int=None,matricularuc=None, desmatricularuc=None,matricularex=None, desmatricularex=None, leerlistaEx=None, leerlistaUc=None):
        super.__init__(ingresar, cedula)
        """La funcion secretaria nos devuelve el poder desmatricular, el matricular y ver listas"""
    pass
class Coordinadora(Matriculacion):
    """clase coordinadora, permisos de leer lista examen y lista de UC"""
    def __init__(self,ingresar:str= None,cedula:int=None,leerlistaEx=None, leerlistaUc=None):
        super.__init__(ingresar, cedula)
        if ingresar == "C" or ingresar =="c":
            
                self.leerUC= leerlistaUc
                self.leerEX= leerlistaEx
        else:
            raise ValueError("No tiene permisos de coordinador/a")
    pass
        
class Estudiante(Matriculacion):
    """clase Estudiante, solo puede matricularse y leer aprobadas y matriculadas al igual que examenes"""
    def __init__(self,ingresar:str= None,cedula:int=None, veraprob=None, verprev=None,matricularuc=None,matricularex=None,):
        super().__init__(ingresar,cedula)
    pass
        
        
    

    

