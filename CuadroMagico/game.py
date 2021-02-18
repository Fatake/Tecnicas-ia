from random import seed
from random import randint
import numpy as np

class Tablero():
    solucion1 = [[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12],
                      [13,14,15,-1]]

    solucionC = None

    def __init__(self, size=4, solucion=None):
        '''
            Crea una matriz de tamaño
            size
            establece una solucion personalizada
        '''
        if solucion != None:
            self.solucionC = solucion
        
        self.size = size

        # inicia la matriz en ceros
        self.matriz = np.zeros((size,size),dtype=int)


    def initTablero(self):
        '''
            Inicia El tablero De forma Random
        '''
        c = 1
        for i in range(0,self.size):
            for j in range(0,self.size):

                while c < 16:
                    valorN = randint(1,(self.size*self.size)-1)

                    if not self.buscaExisteValor(valorN):
                        if self.matriz[i][j] == -1:
                            break
                        c += 1
                        self.matriz[i][j] = valorN
                        break

    def buscaExisteValor(self, valor):
        '''
            Funcion que retorna 
            True si existe el Valor dado
            False si no existe
        '''
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.matriz[i][j] == valor:
                    return True
        return False       

    def ponVacio(self, coordenada):
        '''
            Funcion que dada una coordenada
            [fila,columna]
            Pone un -1 en representacion del Vacio
            Retorna:
            True si se coloca correctamente
            False si no existe la coordenada
        '''

        f,c = coordenada
        
        # Checa si existe la coordenada
        if f < 0 or f > self.size-1:
            return False
        elif c < 0 or c > self.size-1:
            return False
        
        self.coordVacioActual = [f,c]
        self.matriz[f][c] = -1

        return True

    def printTablero(self,string="\t<-----   Tablero Actual  ---->\n"):
        print(string)
        for fila in self.matriz:
            c = 0
            for columna in fila:
                aux = ""
                if columna == -1:
                    aux += "--"
                else:
                    aux += str(columna)
                if c == self.size-1:
                    print(aux, end='')
                else:
                    print(aux+" - ", end='')
                c += 1
            print("\n", end='')

    def mover(self, direccion):
        '''
            u <- up
            d <- down
            l <- left 
            r <- right
        '''
        # Optiene las coordenadas del Vacio actual
        fv,cv = self.coordVacioActual

        nf = 0 # Coordenada Nueva Fila
        nc = 0 # Coordenada Nueva Columna
        
        if direccion == 'u':
            nf = fv - 1
            nc = cv
        elif direccion == 'd':
            nf = fv + 1
            nc = cv
        elif direccion == 'l':
            nf = fv
            nc = cv - 1
        elif direccion == 'r':
            nf = fv
            nc = cv + 1
        
        # Pregunta si puede mover a esa direccion
        if nf < 0 or nf > self.size-1:
            return False
        elif nc < 0 or nc > self.size-1:
            return False

        # Intercambio
        aux = self.matriz[nf][nc] # Guardo el Valor de Destino

        # Se pone en el valor de destino el -1 Vacio
        self.matriz[nf][nc] = -1

        # Se pone en el origen el valor
        self.matriz[fv][cv] = aux

        # Respaldo la coordenada nueva del Vacio
        self.coordVacioActual = [nf,nc]

        return True

    def getSize(self):
        return self.size

