
from random import randint

class Agente():
    def __init__(self,tablero):
        self.tableroActual = tablero
    
    def iaNoInteligente(self):
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

                if self.tableroActual.mover(dir):
                    continue
                else:
                    self.tableroActual.printTablero()
                    print("Movimiento {0} Dir {1}".format((i+1),dir))
                    break