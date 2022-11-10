package main

import (
	"sync"
)

func NewEdges(ints RandInts, nodeNum, edgeNum int) *map[int]*Set[int] {
	type adj struct {
		v     int
		neigs *Set[int]
	}

	c := make(chan adj, nodeNum)

	var wg sync.WaitGroup

	for v := 1; v < nodeNum; v++ {
		wg.Add(1)
		// https://go.dev/doc/effective_go#parallel
		go func(v int) { // let's pretend this is heavy computation, worth spanning a thread...
			defer wg.Done()
			n := edgeNum
			if n > v {
				n = v
			}
			neigs := ints(v, n)
			c <- adj{v, neigs}
		}(v)
	}

	go func() {
		wg.Wait()
		close(c)
	}()

	edges := make(map[int]*Set[int])
	for n := range c {
		edges[n.v] = n.neigs
	}

	return &edges
}

type Node struct {
	id    int
	edges []*Edge
}

type Edge struct {
	neig   *Node
	weight *int
}

func NewGraph(int RandInt, ints RandInts, nodeNum, edgeNum, min, max int) []*Node {
	nodes := make([]*Node, nodeNum)
	edges := *NewEdges(ints, nodeNum, edgeNum)

	for i := 0; i < nodeNum; i++ {
		nodes[i] = &Node{i, make([]*Edge, 0)}

		edg := edges[i]

		if edg == nil {
			continue
		}

		for e := range edg.Iter() {
			weig := int(min, max)

			out := Edge{nodes[e], &weig}
			nodes[i].edges = append(nodes[i].edges, &out)

			in := Edge{nodes[i], &weig}
			nodes[e].edges = append(nodes[e].edges, &in)
		}
	}

	return nodes
}
