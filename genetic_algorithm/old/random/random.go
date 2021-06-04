package random

import (
	"math/rand"
	"time"
)

type (
	BoolType  func(int IntType) bool
	IntType   func(maxValue int) int
	RuneType  func(runes []rune) rune
	RunesType func(n int, runes []rune) []rune
)

func Init() {
	rand.Seed(time.Now().UnixNano())
}

func Int(maxValue int) int {
	return rand.Intn(maxValue)
}

func Rune(runesPool []rune) rune {
	return runesPool[Int(len(runesPool))]
}

func Runes(length int, runesPool []rune) []rune {
	runes := make([]rune, length)
	for i := range runes {
		runes[i] = runesPool[Int(len(runesPool))]
	}
	return runes
}

func Bool(int IntType) bool {
	return int(2) == 1
}
