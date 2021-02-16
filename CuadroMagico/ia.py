
from random import randint
from time import sleep

class Agente():

    def __init__(self,tablero):
        self.tableroActual = tablero
        if self.tableroActual.solucion3 != None:
            self.customSolution = True
        else:
            self.customSolution = False
            
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

    def funcionCosto(self,tablero):
        if self.customSolution:
            objetivo = self.tableroActual.solucion3
        else:
            objetivo = self.tableroActual.solucion1
        
        size = len(tablero)
        peso = 0
        for i in range(0,size):
            for j in range(0,size):
                if objetivo[i][j] == tablero[i][j]:
                    peso += 1
        
        return peso
         

    def mejorMovimiento(self):
        posiblesMovimientos = []
        
        # Hace todos los movimientos posibles y calcula costos
        for i in ['u','d','r','l']:
            futuro = self.tableroActual
            futuro.mover(i)
            costo = self.funcionCosto(futuro.matriz)
            posiblesMovimientos.append([futuro.matriz,costo,i])

        print("Costos:")
        best = 0
        j = 0
        for i in range(4):
            print(posiblesMovimientos[i][1])
            if posiblesMovimientos[i][1] > best:
                j = i
                best = posiblesMovimientos[i][1]
                

        return posiblesMovimientos[j]
        
    def resuelve(self):
        termina = self.tableroActual.getSize()
        termina *= termina
        
        f = 0
        while f < termina:
            aux = self.mejorMovimiento()
            self.tableroActual.mover(aux[2])
            # Costo
            f = aux[1]
            self.tableroActual.printTablero()
            # sleep(1)
