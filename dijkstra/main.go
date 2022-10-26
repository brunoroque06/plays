package main

import (
	"fmt"
)

func init() {
	RandSetup()
}

func main() {
	var i interface{}
	fmt.Println(i)

	graph := NewGraph(Int, Ints, 100, 10, 0, 24)
	for g := range graph {
		fmt.Println(g)
	}
}
