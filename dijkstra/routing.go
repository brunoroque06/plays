package main

import (
	"math"
)

func prim(graph []Node, start int) []Edge {
	path := make([]Edge, 0, len(graph)-1)

	visited := make(map[int]*Node, len(graph))
	visited[graph[start].id] = &graph[start]

	max := math.MaxInt
	longest := Edge{&graph[start], &max}
	for len(path) != len(graph)-1 {
		shortest := longest
		for _, n := range visited { // some redundancy...
			for _, e := range n.edges {
				if _, ok := visited[e.neig.id]; !ok && *e.weight < *shortest.weight {
					shortest = e
				}
			}
		}
		path = append(path, shortest)
		visited[shortest.neig.id] = shortest.neig
	}

	return path
}

func dijkstra(graph []Node, start int) []Edge {
	path := make([]Edge, 0, len(graph)-1)

	type cost struct {
		cost int
		node *Node
	}

	costs := make(map[int]cost, len(graph))
	costs[graph[start].id] = cost{0, &graph[start]}

	for len(path) != len(graph)-1 {
		lowCost := math.MaxInt
		var edge Edge

		for _, c := range costs { // some redundancy...
			for _, e := range c.node.edges {
				if _, ok := costs[e.neig.id]; ok {
					continue
				}
				cost := c.cost + *e.weight
				if cost < lowCost {
					lowCost = cost
					edge = e
				}
			}
		}

		path = append(path, edge)
		costs[edge.neig.id] = cost{lowCost, edge.neig}
	}

	return path
}

func cost(path []Edge) int {
	c := 0
	for _, e := range path {
		c = c + *e.weight
	}
	return c
}
