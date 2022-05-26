##ejercicio 3 Practica
nombres=["antonio","jose", "alberto", "kristy", "elTomy"]
edades= [34, 45, 32, 87, 32]
def may():
    """Esta funcion devuelve el numero mayor de una lista"""
    numero1= 0 
    for i in edades:
        if i > numero1:
            numero1 = i 
    return numero1
def min():
    """esta funcion desvuelve el numero menor de una lista"""
    numero2= 1000
    for x in edades:
        if x < numero2:
            numero2 = x 
    return numero2
def nosequeponeraca(**nolose):
    """Esta funcion se usara para que el usuario sepa cual es la persona mas joven de la lista 'nombres' y su edad, tambien la
    la persona que tenga mayor edad y el nombre"""
    listamayor=[]
    listamenor=[]
    tupla=[] 
    for i in range(len(edades)):
        if min()== edades[i]:
            listamenor.append(nombres[i])
        elif may() == edades[i]:
            listamayor.append(nombres[i])
    tupla.append(listamenor)
    tupla.append(listamayor)
    return tupla     
print(tuple(nosequeponeraca()))