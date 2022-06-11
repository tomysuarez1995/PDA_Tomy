"""Las siguientes imortaciones son las demas clases incorporadas"""
from Matriculacion import Matriculacion
# from Rol import Ingreso
# from Plan_de_Estudio import UnidadCurricular, Plan_Estudio

"""Con estas funciones se ingresan las personas con roles ("tipoRol) como A para administrativa, C para coordinador/a y E como estudiante
con los datos de siguientes:

    nombre:str 
    CI:int 
    tipoRol:str 
    AñoIngreso:int
    
    """
# nuevoalumno= Ingreso(nombre= "Virginia Catala", CI=65782312, tipoRol= "A", AñoIngreso= 2016)
# print(nuevoalumno.guardar_datos())

"""Estas funciones ingresan UC en el plan de estudio con los siguientes datos:
        nombreUC:str 
        semestreUC:int 
        creditosUC:int 
        Codigo:str 
        Previas:list = None si y solo si es de semestre 2 o superior
        Aprobadas:list = None si y solo si es de semestre 3 o superior

"""
# uc1=Plan_Estudio(nombreUC="Electrotecnia", semestreUC= 3, creditosUC= 10, Codigo= "Elect", Previas=["mat2", "fisic2"], Aprobadas=["mat1","Fisic1"])
# print(uc1.ordenar_por_semestre())


"""Con la siguiente linea de codigo se ingresa como usuario en el gestor de matriculacion, donde "ingresar" es referente al tipo de usuario
sabiendo que A o a hace referecia a administrador, C o c hace referencia a coordinador/a y E o e hace referencia al estudiante que entra si y solo si ingresa su cedula para saber a donde dirigir lo guardado.

los datos de ingreso son:
     ingresar:str para todos los tipos de usuarios
     
     cedula:int= para todos los tipos de usuarios
 
 los siguientes argumentos se activan si solo si el tipo de usuario varia, por ejemplo:
 Administrativa/o:
     matricularuc=None 
     desmatricularuc=None
     matricularex=None 
     desmatricularex=None 
     leerlistaEx=None 
     leerlistaUc=None 
     
     
Coordinador/a:
     leerlistaEx=None 
     leerlistaUc=None 
    
Estudiante:
    matricularuc=None
    matricularex=None
    veraprob=None 
    verprev=None
 """
adm1= Matriculacion(ingresar="c", cedula=67876923,)


