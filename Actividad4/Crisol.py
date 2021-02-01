from random import randrange
import os

def sensaTemperatura(temp, gas, vent):
	return (temp + (2 * gas) - (5 * vent))

def aplicarGas(Gas):
    print("[+] Aplicando {0}% de Gas".format(Gas))

def main():
    memoria = open('datos.dat','w+')

    temp = 0
    Gas = 4
    Vent = 0

    memoria.write("Temp    Gas\n")
    print("<-- Iniciando Programa controlador Cristol -->")
    while (True):
        # Sensar
        temp = sensaTemperatura(temp, Gas, Vent)
        print("[i] Temperatura: {0} Gas: {1}".format(temp,Gas))

        str = "{0}    {1}\n".format(temp,Gas)
        memoria.write(str)

        if( temp > 320):
            Vent += 1
            if(Gas != 0):
                print( "[-] Bajando nivel de gas") 
                Gas -= 1
            print ("[+] Aumentando ventilacion")
            
        else:
            if(Vent != 0):
                Vent = 0
                print ("[-] Apagando ventilacion")
            print( "[+] Aumentando nivel de gas") 
            Gas += 1
            aplicarGas(Gas)
        print("\n")

    memoria.close()

if __name__ == "__main__":
    main()