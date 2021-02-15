from random import seed
from random import randint

class Tablero():
    def __init__(self, size=4):
        self.size = size
        self.matriz = []
        self.__initZeros()

    def __initZeros(self):
        '''
            Inicia Todo el tablero en Ceros
        '''
        matriz = []

        # Para Cada Fila
        for i in range(0,self.size):
            col = []
            # Para Cada Columna
            for j in range(0,self.size):
                col.append( 0 )
            matriz.append(col)
        
        self.matriz = matriz

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
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.matriz[i][j] == valor:
                    return True
        return False       

    def ponVacio(self, coordenada):
        f = coordenada[0] - 1
        c = coordenada[1] - 1 
        self.coordVacioActual = [f,c]
        self.matriz[f][c] = -1

    def printTablero(self):
        print("\t<-----   Tablero Actual  ---->\n")
        for fila in self.matriz:
            c = 0
            for columna in fila:
                aux = ""
                if columna == -1:
                    aux += "--"
                else:
                    aux += str(columna)
                if c == 3:
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
        fv = self.coordVacioActual[0] # Coordenada Vacio Fila
        cv = self.coordVacioActual[1] # Coordenada Vacio Columna

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
        
        if nf < 0 or nf > self.size-1:
            # print("\nNo se puede mover en direccion "+direccion)
            return False
        elif nc < 0 or nc > self.size-1:
            # print("\nNo se puede mover en direccion "+direccion)
            return False

        # Intercambio
        aux = self.matriz[nf][nc] # Guardo el Valor de Destino
        # Se pone en el valor de destino el -1 Vacio
        self.matriz[nf][nc] = -1

        # Se pone en el origen el valor
        self.matriz[fv][cv] = aux

        # Respaldo la coordenada nueva del Vacio
        self.coordVacioActual[0] = nf
        self.coordVacioActual[1] = nc
