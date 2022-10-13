package main

import "testing"

func TestCalcNumEdges(t *testing.T) {
	if e := calcNumEdges(3, 0); e != 2 {
		t.Error(e)
	}
	if e := calcNumEdges(4, 30); e != 4 {
		t.Error(e)
	}
	if e := calcNumEdges(4, 100); e != 6 {
		t.Error(e)
	}
}
