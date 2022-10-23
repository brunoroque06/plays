package main

import (
	"math/rand"
	"sort"
	"time"
)

func Setup() {
	// https://github.com/golang/go/issues/54880
	rand.Seed(time.Now().UnixNano())
}

func Intn(min, max int) int {
	return min + rand.Intn(max)
}

func DistinctIntn(max, n int) *[]int {
	if max < 1 || max < n {
		panic("invalid argument")
	}
	pool := make([]int, max)
	for i := range pool {
		pool[i] = i
	}
	// https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
	rand.Shuffle(len(pool), func(a, b int) { pool[a], pool[b] = pool[b], pool[a] })
	sel := pool[0:n]
	sort.Ints(sel)
	return &sel
}
