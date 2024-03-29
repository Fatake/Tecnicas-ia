package main

import (
	"fmt"
	"log"
	"os"
)

// PATHFILE paht del archivo
const PATHFILE string = "datos.dat"

func sensarTemp(temp int, gas int, vent int) int {
	return (temp + (2 * gas) - (5 * vent))
}

func aplicarGas(gas int) {
	fmt.Printf("[+] Aplicando %d de Gas \n", gas)
}

func check(err error) {
	if err != nil {
		log.Println(err)
		os.Exit(-1)
	}
}

func main() {
	memoria, err := os.OpenFile(PATHFILE, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("[!] no existe Datos.dat, creando...")
		_, err := os.OpenFile(PATHFILE, os.O_CREATE, 0666)
		if err != nil {
			log.Fatal(err)
			os.Exit(1)
		}
	}
	defer memoria.Close()

	if _, err := memoria.WriteString("Temp    Gas\n"); err != nil {
		log.Fatal(err)
	}

	temp := 0
	gas := 0
	vent := 0

	fmt.Printf("<-- Iniciando Programa Controlador Crisol -->\n")

	for i := 0; i < 200; i++ {
		// sensor
		temp = sensarTemp(temp, gas, vent)
		fmt.Printf("[i] Temp: %d Gas: %d \n", temp, gas)

		str := fmt.Sprintf("%d    %d", temp, gas)

		if _, err := memoria.WriteString(str); err != nil {
			log.Fatal(err)
		}

		if temp > 320 {
			vent = vent + 3
			fmt.Println("[+] Aumentando Ventilacion")
			if gas != 0 {
				fmt.Println("[-] Bajando nivel de gas")
				gas = gas - 3
			}
		} else {
			if vent != 0 {
				vent = 0
				fmt.Println("[-] Apagando ventilacion")
			}
			gas++
			fmt.Println("[+] Aumentando nivel de gas")
			aplicarGas(gas)
		}
		fmt.Print("\n\n")
		// time.Sleep(250 * time.Millisecond)
	}
	fmt.Print("[----]\n")
}
