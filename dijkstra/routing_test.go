package main

import "testing"

func graph() []Node {
	a := Node{0, make([]Edge, 0)}
	b := Node{1, make([]Edge, 0)}
	c := Node{2, make([]Edge, 0)}

	ab := 3
	ac := 5
	bc := 4

	a.edges = append(a.edges, Edge{&b, &ab}, Edge{&c, &ac})
	b.edges = append(b.edges, Edge{&a, &ab}, Edge{&c, &bc})
	c.edges = append(c.edges, Edge{&a, &ac}, Edge{&b, &bc})

	return []Node{a, b, c}
}

func TestPrim(t *testing.T) {
	g := graph()
	a, b := g[0], g[1]
	path := prim(g, 0)

	if len(path) != 2 {
		t.Error("number of paths")
	}

	if path[0] != a.edges[0] || path[1] != b.edges[1] {
		t.Error("wrong path")
	}
}

func TestDijkstra(t *testing.T) {
	g := graph()
	a := g[0]
	path := dijkstra(g, 0)

	if len(path) != 2 {
		t.Error("number of paths")
	}

	if path[0] != a.edges[0] || path[1] != a.edges[1] {
		t.Error("wrong path")
	}
}
