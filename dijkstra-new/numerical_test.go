package main

import "testing"

func TestToCharBase(t *testing.T) {
	if b := ToCharBase(0); b != "a" {
		t.Error(b)
	}
	if b := ToCharBase(56); b != "ce" {
		t.Error(b)
	}
}

func TestToDecimal(t *testing.T) {
	if d := ToDecimal("a"); d != 0 {
		t.Error(d)
	}
	if d := ToDecimal("h"); d != 7 {
		t.Error(d)
	}
	if d := ToDecimal("ce"); d != 56 {
		t.Error(d)
	}
}
