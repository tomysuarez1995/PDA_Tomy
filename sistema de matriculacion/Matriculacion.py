from debugpy import listen
from Rol import Ingreso
from Plan_de_Estudio import UnidadCurricular, Plan_Estudio
# class Matriculacion():
#     """Esta clase se utiliza para matricular o desmatricular y ver listas"""
#     def __init__(self,inscribirseUC, inscribirseEx, listaUc, listaEx, mostrarPrevias, mostrarAprob, desmatricUC, desmatricEx ):
#         pass

#     def matricularUC(self):
#         pass
#     def matricularEX(self):
#         pass
#     def desmatricularUC(self):
#         pass
#     def desmatricularEx(self):
#         pass
#     def ver_listaUC(self):
#         pass
#     def ver_listaEx(self):
#         pass

def obt_admin():
    rol = open("Rol\dmin.txt", "r")
    for linea in rol:
        list1= linea.split()[1::2]
        list2=linea.split()[::2]
        list2.pop(0)
        diccadmin= dict(zip(list1, list2))
    rol.close()
    return diccadmin
        
        
def obt_coord():
    rol = open("Rol\coord.txt", "r")
    for linea in rol:
        list1= linea.split()[1::2]
        list2=linea.split()[::2]
        list2.pop(0)
        dicccoord= dict(zip(list1, list2))
    rol.close()
    return dicccoord
    
def obt_alum():
    listEstud=[]
    rol = open("Rol\estudiante.txt", "r")
    for linea in rol:
        list1= linea.split()[1::2]
        list2=linea.split()[::2]
        list2.pop(0)
        diccest= dict(zip(list1, list2))
        del diccest["rol"]
        listEstud.append(diccest)
    rol.close()
    return listEstud 


# print(obt_admin())
# print(obt_coord())
#print(obt_alum())
