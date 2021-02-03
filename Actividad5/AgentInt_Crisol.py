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
  
    if ( len(posibles) == 0 ):
        print("[i] Temperatura No encontrada en Historico")
        return randrange(4)+1

    print("[i] Temperaturas encontradas en Historico {0}".format(len(posibles)))
    # print(posibles)

    p = 0 # apuntador al indice mejor
    aux = 0 # Auxiliar para saber cual es el mayor
    tempF = 0
    for i in range (0,11,1):
        tempF = posibles[i][2]

        if(tempF <= 320  ):
            aux = tempF
            p = i
            
    # print("[i] Mejor Temperatura Temp Futura {0} a {1}% de gas".format(aux,posibles[p][1]))
    return posibles[p][1]

def main(historico):
    memoria = open('datos.dat','w+')
    temp = 0 # maximo hasta 320
    Gas = 0 # 4 representa un 4 %
    Vent = 0 # 1 prendido 0 Apagado

    # Cuando vent = 1 entonces Gas se baja al 0%
    memoria.write("Temp,Gas\n")
    print("<-- Agente Inteligente Cristol -->")
    
    for i in range(300):
        # Sensar
        temp = sensaTemperatura(temp, Gas, Vent)
        
        print("[i] Temp Actual: {0}, % de Gas: {1}".format(temp,Gas))

        nivelGas = busca(historico,temp)
        str = "{0},{1}\n".format(temp,Gas)
        memoria.write(str)
        
        # Pregunta sobre la temperatura
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
    memoria.close()

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
    # print("[*] Datos Optenidos")
    # print(historico)
    main(historico)
