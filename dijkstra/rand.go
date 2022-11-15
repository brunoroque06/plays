package main

import (
	"math/rand"
	"time"
)

func RandSetup() {
	// https://github.com/golang/go/issues/54880
	rand.Seed(time.Now().UnixNano())
}

type RandInt func(min, max int) int

func Int(min, max int) int {
	return min + rand.Intn(max)
}

type RandInts func(v, n int) *Set[int]

func Ints(max, n int) *Set[int] {
	if max < 1 || max < n {
		panic("invalid argument")
	}
	sel := MakeSet[int]()
	for sel.Len() != n {
		i := Int(0, max)
		if !sel.Has(i) {
			sel.Add(i)
		}
	}
	return &sel
}
