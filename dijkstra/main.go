package main

import (
	"fmt"
)

func init() {
	RandSetup()
}

func main() {
	graph := NewGraph(Int, Ints, 1000, 10, 1, 24)

	primPath := prim(graph, 0)
	dijkstraPath := dijkstra(graph, 0)

	fmt.Printf("Cost Prim: %d\n", cost(primPath))
	fmt.Printf("Cost Dijkstra: %d\n", cost(dijkstraPath))
}
