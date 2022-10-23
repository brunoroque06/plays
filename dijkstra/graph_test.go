package main

import "testing"

func TestCreateEdges(t *testing.T) {
	dist := func(v, n int) *[]int {
		nums := make([]int, n, n)
		return &nums
	}
	edges := *createEdges(dist, 15, 10)
	if len(edges) != 14 {
		t.Error()
	}
	if len(*edges[1]) != 1 {
		t.Error()
	}
	if len(*edges[14]) != 10 {
		t.Error()
	}
}
