
def sensaTemperatura(temp, gas, vent):
	return (temp + (2 * gas) - (5 * vent))

def aplicarGas(Gas):
    print("[+] Aplicando {0}% de Gas".format(Gas))

def main():
    memoria = open('datos.dat','w+')

    temp = 0 # maximo hasta 320
    Gas = 0 # 4 representa un 4 %
    Vent = 0 # 1 prendido 0 Apagado

    # Cuando vent = 1 entonces Gas se baja al 0%

    memoria.write("Temp    Gas\n")
    print("<-- Iniciando Programa controlador Cristol -->")
    
    for i in range(300):
        # Sensar
        temp = sensaTemperatura(temp, Gas, Vent)
        
        print("[i] Temperatura: {0} Gas: {1}".format(temp,Gas))

        # Registra
        str = "{0}    {1}\n".format(temp,Gas)
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
                
            print( "[+] Aumentando nivel de gas") 
            Gas += 10
            
            # Actua
            aplicarGas(Gas)
        print("\n")

    memoria.close()

if __name__ == "__main__":
    main()