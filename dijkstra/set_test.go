package main

import (
	"testing"
)

func TestSet(t *testing.T) {
	set := makeSet()
	if set.Has(8) || set.Len() != 0 {
		t.Error()
	}
	k := 4
	set.Add(k)
	if !set.Has(k) || set.Len() != 1 {
		t.Error()
	}
	if set.Del(8) == nil {
		t.Error()
	}
	set.Del(k)
	if set.Len() != 0 {
		t.Error()
	}
}
