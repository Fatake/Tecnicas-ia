package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"time"
)

var pathFile string = "datos.dat"

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
	bw := []byte("Temp    Gas\n")
	err := ioutil.WriteFile(pathFile, bw, 0777)
	check(err)
	temp := 0
	gas := 0
	vent := 0
	fmt.Printf("<-- Iniciando Programa Controlador Crisol -->\n")
	memoria, err := os.OpenFile(pathFile, os.O_APPEND|os.O_WRONLY, 0644)
	check(err)

	for i := 0; i < 200; i++ {
		temp = sensarTemp(temp, gas, vent)
		fmt.Printf("[i] Temp: %d Gas: %d \n", temp, gas)

		str := "" + strconv.Itoa(temp) + "    " + strconv.Itoa(gas) + "\n"

		if _, err := memoria.WriteString(str); err != nil {
			log.Fatal(err)
		}

		if temp > 320 {
			vent++
			fmt.Println("[+] Aumentando Ventilacion")
			if gas != 0 {
				fmt.Println("[-] Bajando nivel de gas")
				gas--
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
		time.Sleep(1 * time.Second)
	}
	defer memoria.Close()
	fmt.Print("[----]\n")
}
