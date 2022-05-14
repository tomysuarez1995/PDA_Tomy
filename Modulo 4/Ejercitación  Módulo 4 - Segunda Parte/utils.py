def graficar(signal, fm, t1 = 0, t2 = 10, title = "Señal de Fotoplestimografía"):
    import matplotlib.pyplot as plt
    import numpy as np
    totalLenght = len(signal)
    if t1 <0 or t2 < 0 or t2 < t1 or t1 == t2 or t1 > totalLenght or t2 == totalLenght > totalLenght:
        raise ValueError("t1 y/o t2 están mal")

    else:
        T = 1.0/fm #período de la señal
        totalLenght = len(signal)

        t = np.arange(int(t1*fm), int(t2*fm))*T

        plt.plot(t, signal[int(t1*fm):int(t2*fm)])
        plt.xlabel("Tiempo [seg]")   # Inserta el título del eje X
        plt.ylabel("Abosrobacia [%]")   # Inserta el título del eje Y
        plt.title(title)

        plt.show()

def crearMatrix(dimensiones:tuple = None):
    """Genera una matriz de ceros utilizando la función zeros de numpy"""
    if dimensiones:
        from numpy import zeros
        matrix = zeros(dimensiones)
        del zeros
        return matrix
    else:
        raise ValueError("No se ha dado ninguna dimensión")

def main():
    import numpy as np
    file = open("plethysmography.txt", "r")

    plesti = file.read().split()

    plesti = np.array([float(valor) for valor in plesti])
    fm = 125
    graficar(plesti, fm, t1 = 300.1, t2 = 305.5, title = "Señal de Fotoplestimografía")

if __name__ == "__main__": 
    main()

