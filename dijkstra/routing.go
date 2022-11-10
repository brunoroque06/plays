package main

import (
	"math"
)

func prim(graph []*Node, start int) []*Edge {
	path := make([]*Edge, 0, len(graph)-1)

	visited := MakeSet[*Node]()
	visited.Add(graph[start])

	max := math.MaxInt
	longest := Edge{graph[start], &max}
	for len(path) != len(graph)-1 {
		shortest := &longest
		for n := range visited.Iter() { // some redundancy...
			for _, e := range n.edges {
				if !visited.Has(e.neig) && *e.weight < *shortest.weight {
					shortest = e
				}
			}
		}
		path = append(path, shortest)
		visited.Add(shortest.neig)
	}

	return path
}

func dijkstra(graph []*Node, start int) []*Edge {
	path := make([]*Edge, 0, len(graph)-1)

	costs := make(map[*Node]int, len(graph))
	costs[graph[start]] = 0

	for len(path) != len(graph)-1 {
		lowCost := math.MaxInt
		var edge *Edge

		for n, nCost := range costs { // some redundancy...
			for _, e := range n.edges {
				if _, ok := costs[e.neig]; ok {
					continue
				}
				cost := nCost + *e.weight
				if cost < lowCost {
					lowCost = cost
					edge = e
				}
			}
		}

		path = append(path, edge)
		costs[edge.neig] = lowCost
	}

	return path
}

func cost(path []*Edge) int {
	c := 0
	for _, e := range path {
		c = c + *e.weight
	}
	return c
}
