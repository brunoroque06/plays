package main

import "testing"

var min = 0
var max = 100
var n = 10

func TestIntn(t *testing.T) {
	num := Intn(min, max)
	if num < min || num > max {
		t.Errorf("outside of bounds")
	}
}

func TestDistinctIntn(t *testing.T) {
	if len(DistinctIntn(min, max, n)) != n {
		t.Errorf("wrong length")
	}
	ints := DistinctIntn(min, max, n)
	for i, _ := range ints {
		if i < min || i >= max {
			t.Errorf("outside of bounds")
		}
	}
}
