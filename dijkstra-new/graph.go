package main

import "math"

func calcNumEdges(n, den int) int {
	nf := float64(n)
	denf := float64(den)
	d := (denf / 100) * ((nf*(nf-1))/2 - nf + 1)
	return int(nf - 1 + math.Round(d))
}
