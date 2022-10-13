package main

import (
	"golang.org/x/exp/slices"
	"math"
)

var abc = []rune("abcdefghijklmnopqrstuvwxyz")
var abcLen = len(abc)

func ToCharBase(num int) string {
	var base []rune
	for quo := num / abcLen; ; quo = quo / abcLen {
		rem := num % abcLen
		base = append(base, abc[rem])
		if quo == 0 {
			break
		}
		num = quo
	}

	for i, j := 0, len(base)-1; i < j; i, j = i+1, j-1 {
		base[i], base[j] = base[j], base[i]
	}

	return string(base)
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func ToDecimal(base string) int {
	dec := 0
	baseLen := len(base)
	for i, d := range base {
		idx := slices.IndexFunc(abc, func(c rune) bool { return c == d })
		dec = dec + idx*pow(abcLen, baseLen-i-1)
	}

	return dec
}
