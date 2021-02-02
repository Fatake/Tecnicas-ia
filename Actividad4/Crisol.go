package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("datos.dat")
	// if our program was unable to read the file
	// print out the reason why it can't
	if err != nil {
		fmt.Println(err)
	}

	// if it was successful in reading the file then
	// print out the contents as a string
	fmt.Print(string(data))

}
