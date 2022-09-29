package main

import "testing"

func TestInt(t *testing.T) {
	min := 0
	max := 10
	num := genInt(min, max)
	if num < min || num > max {
		t.Errorf("Outside of range [%d, %d]: %d", min, max, num)
	}
}

func TestInts(t *testing.T) {
	n := 3
	if len(genInts(0, 18, n)) != n {
		t.Errorf("Wrong length")
	}
}
