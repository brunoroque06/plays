package main

import "math/rand"

func genInt(min int, max int) int {
	return min + rand.Intn(max)
}

func genInts(min int, max int, n int) []int {
	nums := make([]int, n)
	for i := range nums {
		nums[i] = genInt(min, max)
	}
	return nums
}
