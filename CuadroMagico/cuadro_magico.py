from random import seed
from random import randint
import game as g
import ia


def main():
    print("\t<-----   Iniciando Cuadro Magico   ----->")
    tablero = g.Tablero()
    if not tablero.ponVacio([2,1]):
        print("[!] Error al poner el vacio, coordenadas no existentes\n\n")
        exit(1)

    tablero.initTablero() 
    tablero.printTablero("\t<-----   Tablero Inicial  ---->\n")

    agente = ia.Agente(tablero)

    agente.resuelve()


if __name__ == '__main__':
    main()
