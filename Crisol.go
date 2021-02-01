package main

import (
	"fmt"
	"io/ioutil"
)

func check(e error) {
	fmt.Printf("[!] Error %s", e)
	if e != nil {
		panic(e)
	}
}

func main() {
	temp := 0.0
	Gas := 4.0
	Vent := 0.0
	fmt.Println("Iniciando Programa controlador Cristol")

	for {
		// Sensar
		temp = sensaTemperatura(temp, Gas, Vent)
		
		if Temp > 320 {
			Vent
		} else {
			Gas := 4
			Aplicar_Gat(Gas)
		}

	}

	dat, err := ioutil.ReadFile("datos.dat")
	check(err)
	fmt.Print(string(dat))

}

func sensaTemperatura(temp float64, gas float64, vent float64) float64 {
	return (temp + (2 * gas) - (5 * vent))
}
