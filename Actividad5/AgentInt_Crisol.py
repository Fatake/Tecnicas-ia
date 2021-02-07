from random import randrange

def sensaTemperatura(temp, gas, vent):
	return (temp + (2 * gas) - (5 * vent))

def aplicarGas(Gas):
    print("[+] Aplicando {0}% de Gas".format(Gas))

def busca(historico, temp):
    posibles = []
    for dato  in historico:
        if (temp == dato[0]):
            posibles.append(dato)
    aux = len(posibles)
    
    # Si no hay datos entonces regresa una pequeña cantidad de gas
    if ( aux == 0 ):
        print("[i] Temperatura No encontrada en Historico")
        return randrange(4)+1

    print("[i] Temperaturas encontradas en Historico {0}".format(aux))

    # Busca cual es la mejor cantidad de gas
    p = 0 # apuntador al indice mejor
    for i in range (0,aux,1):
        if(posibles[i][2] <= 320  ):
            p = i

    return posibles[p][1]

def main(historico):

    temp = 0 # maximo hasta 320
    Gas = 0 # 4 representa un 4 %
    Vent = 0 # 1 prendido 0 Apagado

		with open('datos.dat','w+') as memoria:
			# Cuando vent = 1 entonces Gas se baja al 0%
			memoria.write("Temp,Gas\n")
			print("<-- Agente Inteligente Cristol -->")
			
			for i in range(300):
					# Sensar
					temp = sensaTemperatura(temp, Gas, Vent)
					print("[i] Temp Actual: {0}, % de Gas: {1}".format(temp,Gas))

					# Se pregunta si existe en el pasado
					nivelGas = busca(historico,temp)

					# Guarda En memoria
					str = "{0},{1}\n".format(temp,Gas)
					memoria.write(str)
					
					# Pregunta Si hizo lo correcto
					if( temp > 320):
							Vent = 1
							if(Gas != 0):
									Gas = 0
									print( "[-] Gas al 0% ") 

							print ("[+] Ventilacion prendida")
					else:
							if(Vent != 0):
									Vent = 0
									print ("[-] Ventilacion Apagada")
							
							if(Gas > nivelGas):
									print( "[+] Disminuyendo Nivel de gas") 
							else:
									print( "[+] Aumentando nivel de gas") 

							Gas = nivelGas
							# Actua
							aplicarGas(Gas)
							
							if(Gas == 0):
									Vent = 1
					print("\n")


def creaTabla():
    file = open('Tabla.csv','w+')

    file.write("t/g,0,10,20,30,40,50,60,70,80,90,100\n")

    print("<-- Haciendo Prueba Inicial -->")
    historial = []
    # Para cada Temperatura
    for temp in range(0,330,10):
        f = True
        # Cada Porcentaje de Gas
        for gas in range(0,110,10):
            aux = ""
            if (f):
                f = False
                aux += ""+str(temp)
            aux += ","+str(sensaTemperatura(temp, gas, 0))
            file.write(aux)
            historial.append([temp,gas,sensaTemperatura(temp, gas, 0)])
        file.write("\n")

    file.close()
    return historial

if __name__ == "__main__":
    historico = creaTabla()
    main(historico)
