package main

import (
	"sync"
)

type adj struct {
	v     int
	neigs *[]int
}

func createEdges(dist func(v int, n int) *[]int, ver, edg int) *map[int]*[]int {
	c := make(chan adj, ver)

	var wg sync.WaitGroup

	for v := 1; v < ver; v++ {
		wg.Add(1)
		go func(v int) { // let's pretend this is heavy computation; worth spanning a thread...
			defer wg.Done()
			n := edg
			if n > v {
				n = v
			}
			neigs := dist(v, n)
			c <- adj{v: v, neigs: neigs}
		}(v)
	}

	go func() {
		wg.Wait()
		close(c)
	}()

	edges := make(map[int]*[]int, 0)
	for n := range c {
		edges[n.v] = n.neigs
	}

	return &edges
}
