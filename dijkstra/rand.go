package main

import (
	"math/rand"
	"time"
)

func Setup() {
	// https://github.com/golang/go/issues/54880
	rand.Seed(time.Now().UnixNano())
}

func Intn(min, max int) int {
	return min + rand.Intn(max)
}

func Intns(max, n int) *Set {
	if max < 1 || max < n {
		panic("invalid argument")
	}
	sel := makeSet()
	for sel.Len() != n {
		i := Intn(0, max)
		if !sel.Has(i) {
			sel.Add(i)
		}
	}
	return sel
}
