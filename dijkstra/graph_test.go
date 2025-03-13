package main

import "testing"

var randInts = func(max, n int) *Set[int] {
	nums := MakeSet[int]()
	for i := range n {
		nums.Add(i)
	}
	return &nums
}

func TestNewEdges(t *testing.T) {
	edges := NewEdges(randInts, 15, 10)
	if len(edges) != 14 {
		t.Error()
	}
	if e := edges[1]; e.Len() != 1 {
		t.Error()
	}
	if e := edges[14]; e.Len() != 10 {
		t.Error()
	}
}

func TestNewGraph(t *testing.T) {
	randInt := func(min, max int) int {
		return max
	}

	g := NewGraph(randInt, randInts, 3, 3, 0, 10)

	if len(g) != 3 {
		t.Error()
	}

	if g[0].id != 0 {
		t.Error()
	}

	if &g[0] != g[0].edges[0].neig.edges[0].neig { // beautiful Oo
		t.Error()
	}

	if &g[1] != g[0].edges[0].neig {
		t.Error()
	}
}
