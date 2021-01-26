package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"time"
)

func check(e error) {
	fmt.Printf("[!] Error %s", e)
	if e != nil {
		panic(e)
	}
}

func main() {
	temp := 0
	fmt.Println("Iniciando Programa controlador Cristol")

	for {
		temp = rand.Intn(360)
		fmt.Printf("Entero %d\n", temp)
		time.Sleep(1 * time.Second)
		if temp == 360 {
			break
		}
	}

	dat, err := ioutil.ReadFile("datos.dat")
	check(err)
	fmt.Print(string(dat))

}

func sensaTemperatura(temp float32, gas float32, vent float32) float32 {
	return (temp + (2 * gas) - (5 * vent))
}
