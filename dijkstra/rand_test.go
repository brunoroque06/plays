package main

import (
	"sort"
	"testing"
)

var min = 0
var max = 100
var n = 10

func TestIntn(t *testing.T) {
	Setup()
	num := Intn(min, max)
	if num < min || num > max {
		t.Errorf("outside of bounds")
	}
}

func TestDistinctIntn(t *testing.T) {
	Setup()
	ints := DistinctIntn(max, n)
	if len(*ints) != n {
		t.Errorf("wrong length")
	}
	for i := range *ints {
		if i < min || i >= max {
			t.Errorf("outside of bounds")
		}
	}
	if !sort.IntsAreSorted(*ints) {
		t.Errorf("not sorted")
	}
}
