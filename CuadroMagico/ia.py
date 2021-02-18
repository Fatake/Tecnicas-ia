
from random import randint
from time import sleep
import copy

class Agente():

    def __init__(self,tablero):
        self.tableroActual = tablero
        if self.tableroActual.solucionC != None:
            self.customSolution = True
        else:
            self.customSolution = False

    def funcionCosto(self,tablero):
        # Pregunta si existe una solucion diferente a la 1
        if self.customSolution:
            objetivo = self.tableroActual.solucionC
        else:
            objetivo = self.tableroActual.solucion1
        
        size = len(tablero)
        peso = 0
        for i in range(0,size):
            for j in range(0,size):
                if objetivo[i][j] == tablero[i][j]:
                    peso += 1
        
        return peso
         

    def mejorMovimiento(self,anterior,verbose=False):
        posiblesMovimientos = []
        
        # Hace todos los movimientos posibles y calcula costos
        for i in ['u','d','r','l']:
            # Crea una copia en diferente lugar de memoria
            futuro = copy.deepcopy(self.tableroActual)

            # Mueve a esa direccion
            futuro.mover(i)
            
            # Optiene el costo
            costo = self.funcionCosto(futuro.matriz)

            # Apendiza costo y movimiento
            posiblesMovimientos.append([costo,i])

        # Para calcular los mejores
        best = 0
        j = 0
        # Para cada costo 
        for i in range(4):
            # Si el costo actual es mejor que el anterior y
            # el movimiento no es el mismo que el anterior
            if posiblesMovimientos[i][0] >= best and posiblesMovimientos[i][1] != anterior:
                # Guarda el Apuntador
                j = i

                # Se queda con el mejor
                best = posiblesMovimientos[i][0]

        if verbose:
            print(posiblesMovimientos)
            print("Best: ",posiblesMovimientos[j]) 

        # Retorna el mejor movimiento
        return posiblesMovimientos[j][1]
        
    def resuelve(self):
        # Tablero Inicial
        inicial = copy.deepcopy(self.tableroActual)

        # Temina cuando llegue al Objetivo
        termina = self.tableroActual.getSize()
        termina *= termina
        anterior = ""

        f = 0
        while f < 1:
            # Calcula el mejor movimiento
            newMovimiento = self.mejorMovimiento(anterior,True)
            
            # Mueve el tablero
            self.tableroActual.mover(newMovimiento)

            # Guarda el movimiento anterior
            anterior = newMovimiento

            self.tableroActual.printTablero()

            print("\t<----------------------------->\n")
            f += 1

        inicial.printTablero("\t<-----   Tablero Inicial  ---->\n")
        self.tableroActual.printTablero("\t<-----   Tablero Final  ---->\n")

