from random import seed
from random import randint
import game as g

def iaNoInteligente(tablero):
    print("\n\t<-----   Iniciando IA Tonta   ----->\n")

    for i in range(50):
        while True:
            val = randint(1,4)
            if val == 1:
                dir = 'u'
            elif val == 2:
                dir = 'd'
            elif val == 3:
                dir = 'r'
            elif val == 4:
                dir = 'l'

            if tablero.mover(dir):
                continue
            else:
                tablero.printTablero()
                print("Movimiento {0} Dir {1}".format((i+1),dir))
                break


def main():
    print("\t<-----   Iniciando Cuadro Magico   ----->")
    tablero = g.Tablero()
    tablero.ponVacio([3,2])

    tablero.initTablero()
    tablero.printTablero()

    iaNoInteligente(tablero)
    tablero.printTablero()

if __name__ == '__main__':
    main()
    