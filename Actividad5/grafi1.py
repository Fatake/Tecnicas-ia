import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

PATH = "datos1.dat"

def openFile():
    
    try:
        file = open(PATH,"r")
    except:
        print("[!] Error en la apertura del Archivo "+PATH)
        os.exit(1)

    lineas = file.readlines()
    i = 1
    time = []
    temp = []
    gas = []
    f = False
    for linea in lineas:
        if(not f):
            f = True
            continue
        aux = linea.split(",")
        temp.append(int(aux[0]))
        gas.append(int(aux[1].replace("\n","")))
        time.append(i)
        i += 1
    return temp, gas , time


def main():
    temp, gas, time = openFile()
    print(temp)
    print("\n")
    print(gas)

    fig, ax = plt.subplots()
    ax.plot(time, temp)

    ax.set(xlabel='Tiempo (s)°', ylabel='Temperatura',
        title='Crisol Agente Bien Informado Temperatura')
    ax.grid()

    fig.savefig("temp.png")

    fig2, ax2 = plt.subplots()

    ax2.plot(time, gas)
    ax2.set(xlabel='Tiempo (s)°', ylabel='% De Gas',
        title='Crisol Agente Bien Informado % de Gas')
    ax2.grid()

    fig2.savefig("gas.png")
    plt.show()

if __name__ == "__main__":
    main()