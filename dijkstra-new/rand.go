package main

import (
	"math/rand"
	"time"
)

func Intn(min int, max int) int {
	return min + rand.Intn(max)
}

func DistinctIntn(min int, max int, n int) []int {
	if min < 0 || max-min < n {
		panic("invalid argument")
	}
	pool := make([]int, max-min)
	for i := range pool {
		pool[i] = min + i
	}
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(pool), func(a, b int) { pool[a], pool[b] = pool[b], pool[a] })
	return pool[0:n] // sort?
}
