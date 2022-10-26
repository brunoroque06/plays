package main

import (
	"testing"
)

var min = 0
var max = 100
var n = 10

func TestIntn(t *testing.T) {
	RandSetup()
	num := Int(min, max)
	if num < min || num > max {
		t.Errorf("outside of bounds")
	}
}

func TestDistinctIntn(t *testing.T) {
	RandSetup()
	ints := Ints(max, n)
	if ints.Len() != n {
		t.Errorf("wrong length")
	}
	for i := range ints.Iter() {
		if i < min || i >= max {
			t.Errorf("outside of bounds")
		}
	}
}
