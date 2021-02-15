from random import seed
from random import randint
import game as g
import ia


def main():
    print("\t<-----   Iniciando Cuadro Magico   ----->")
    tablero = g.Tablero()
    tablero.ponVacio([3,2])

    tablero.initTablero()
    tablero.printTablero()

    agente = ia.Agente(tablero)

    agente.iaNoInteligente()


if __name__ == '__main__':
    main()