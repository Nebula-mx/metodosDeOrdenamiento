# graficar.py
import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    # 1. PON AQUÍ LOS DOS CSV QUE VAS A PONER A PELEAR
    datos = pd.read_csv("burbuja_tiempo.csv", sep=";")
    datosDos = pd.read_csv("insercion_tiempo.csv", sep=";")
    
    x = datos.N
    y = datos.Tiempo
    yy = datosDos.Tiempo
    
    plt.plot(x, y, x, yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    
    # 2. CAMBIA EL TÍTULO Y LA LEYENDA SEGÚN QUIÉNES ESTÉN PELEANDO
    plt.title("Burbuja Vs Insercion")
    plt.legend(('Burbuja', 'Insercion'), prop={'size':10}, loc='upper left')
    
    plt.grid()
    plt.show()
