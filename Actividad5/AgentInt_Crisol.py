
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
    print("<-- Agente Simple Cristol -->")
    
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
            historial.append([temp,gas])
        file.write("\n")

    file.close()
    return historial

if __name__ == "__main__":
    historico = creaTabla()
    print("[*] Datos Optenidos")
    print(historico)
    # main()
