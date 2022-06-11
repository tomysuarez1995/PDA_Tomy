import Plan_de_Estudio
class Ingreso():
    """En esta clase se asigna el rol y se agregan a la base de datos a los estudiantes, docentes, coordinadores
    y administrativa"""
    def __init__(self, nombre:str, CI:int, tipoRol:str, AñoIngreso:int):
        """constructor"""
        if tipoRol == "A" or tipoRol == "E" or tipoRol == "C":
            self.nomb=nombre
            self.ci= CI
            self.tipo= tipoRol
            self.ingreso = AñoIngreso
        else:
            raise ValueError("el rol debe de ser E(Estudiante), A(Administrativa), C(Coordinadora)")
   
    def def_rol(self):
        rol=""
        if self.tipo == "A":
            rol= 1
        elif self.tipo == "C":
            rol=2
        elif self.tipo == "E":
            rol=3
        return rol

    def adquirir_nomb(self):
        return self.nomb

    def adquirir_ci(self):
        return self.ci

    def mostrar_rol(self):
        tipo= ""
        if self.tipo == "A":
            tipo= "Administrativa/o"
        elif self.tipo == "E":
            tipo= "Estudiante"
        else:
            tipo= "Coordinador/a"
        return tipo
    
    def mostrar_ano(self):
        return self.ingreso

    def def_permisos(self):
        if self.def_rol() == 1:
            return f"el {self.mostrar_rol()} tiene permisos de Escritura y Lectura"
        elif self.def_rol() == 2:
            return f"el {self.mostrar_rol()} tiene permisos de Lectura"
        elif self.def_rol() == 3:
            return f"el {self.mostrar_rol()} no tiene permisos"
        
    def asignar_mail(self):
        if self.def_rol() == 3:
            correo = self.nomb.replace(" ", ".")
            return f"{correo}@estudiantes.utec.edu.uy"
        else:
            correo = self.nomb.replace(" ", ".")
            return f"{correo}@utec.edu.uy"

    def mostrar_datos(self):
        """en esta funcion se muestran los datos del agregado"""
        return f"{self.adquirir_nomb()} con cedula {self.adquirir_ci()} tiene los datos: \nrol: {self.mostrar_rol()} \npermisos: {self.def_permisos()} \ncorreo: {self.asignar_mail()}"
    
    def guardar_datos(self):
        if self.def_rol() == 1:
            texto= open("rol.txt", "a")
            texto.write(f"{self.mostrar_rol()} {self.adquirir_nomb()} cedula {self.adquirir_ci()} ingreso {self.mostrar_ano()} rol {self.def_rol()} correo {self.asignar_mail()} \n")
            texto.close()
            return "Administrativa/o guardado"

        if self.def_rol() == 2:
            texto= open("rol.txt", "a")
            texto.write(f"{self.mostrar_rol()} {self.adquirir_nomb()} cedula {self.adquirir_ci()} ingreso {self.mostrar_ano()} rol {self.def_rol()} correo {self.asignar_mail()} \n")
            texto.close()
            return "Coordinador/a Guardado"
        else:
            texto= open("rol.txt", "a")
            texto.write(f"{self.mostrar_rol()} {self.adquirir_nomb()} cedula {self.adquirir_ci()} ingreso {self.mostrar_ano()} rol {self.def_rol()} correo {self.asignar_mail()} \n")
            texto.close()
            return "Estudiante Guardado"


