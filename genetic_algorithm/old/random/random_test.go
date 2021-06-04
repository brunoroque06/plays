package random

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

var runesPool = []rune("abc")

func TestRandomRune(t *testing.T) {
	randomRune := Rune(runesPool)
	assert.True(t, strings.ContainsRune(string(runesPool), randomRune))
}

func TestRandomRunes(t *testing.T) {
	size := 10
	runes := Runes(size, runesPool)
	assert.Equal(t, size, len(runes))
}

func Test_WhenIntIs0_ThenFalse(t *testing.T) {
	randomInt := func(maxValue int) int { return 0 }
	boolean := Bool(randomInt)
	assert.False(t, boolean)
}

func Test_WhenIntIs1_ThenTrue(t *testing.T) {
	randomInt := func(maxValue int) int { return 1 }
	boolean := Bool(randomInt)
	assert.True(t, boolean)
}
