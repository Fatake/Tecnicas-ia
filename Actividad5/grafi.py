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
    return temp, gas


def main():
    temp, gas = openFile()
    print(temp)
    print("\n")
    print(gas)

    fig, ax = plt.subplots()
    ax.plot(temp, gas)

    ax.set(xlabel='temperatura C°', ylabel='% de Gas',
        title='Crisol Agente Simple')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

if __name__ == "__main__":
    main()