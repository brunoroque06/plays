package individual

import (
	"testing"

	"github.com/brunoroque06/geneticalgorithm/random"
	"github.com/stretchr/testify/assert"
)

func TestRandomIndividualCreation(t *testing.T) {
	genes := []rune("abc")
	randomRunes := func(n int, runes []rune) []rune { return genes }

	individual := NewRandomIndividual(18, []rune(""), randomRunes)

	assert.Equal(t, genes, individual.Genes)
}

func Test_GivenSameRandomRunes_WhenGeneratingIndividuals_ThenIndividualsAreEqual(t *testing.T) {
	numberOfIndividuals := 18
	genes := []rune("abc")
	randomGenes := func(n int, runes []rune) []rune { return genes }

	individuals := NewRandomIndividuals(18, []rune(""), randomGenes, numberOfIndividuals)

	assert.Equal(t, numberOfIndividuals, len(individuals))
	assert.True(t, areIndividualsEqual(individuals, genes))
}

func areIndividualsEqual(individuals []*Individual, genes []rune) bool {
	areGenesEqual := true
	for _, individual := range individuals {
		if string(individual.Genes) != string(genes) {
			areGenesEqual = false
			break
		}
	}
	return areGenesEqual
}

func Test_GivenGenesWithLength2AndIndividualGenesWithLength3_WhenEstimateFitness_ThenError(t *testing.T) {
	target := []rune("abc")
	individual := Individual{target[0:1]}

	fitness, err := individual.EstimateFitness(target)

	assert.Equal(t, float32(-1), fitness)
	assert.NotNil(t, err)
}

func TestFitnessEstimation(t *testing.T) {
	target := []rune("abc?")
	individual := Individual{[]rune("abc_")}

	fitness, err := individual.EstimateFitness(target)

	assert.Equal(t, float32(0.75), fitness)
	assert.Nil(t, err)
}

func Test_GivenParentsWithDifferentGenesLength_WhenCrossover_ThenError(t *testing.T) {
	parentX := Individual{[]rune("abc")}
	parentY := Individual{[]rune("de")}

	_, err := Crossover(&parentX, &parentY, func(int random.IntType) bool { return true })

	assert.NotNil(t, err)
}

func TestCrossover(t *testing.T) {
	parentX := Individual{[]rune("abc")}
	parentY := Individual{[]rune("def")}

	child, err := Crossover(&parentX, &parentY, func(int random.IntType) bool { return true })

	assert.True(t, isChildLegit(&parentX, &parentY, child))
	assert.Nil(t, err)
}

func isChildLegit(parentX *Individual, parentY *Individual, child *Individual) bool {
	if len(child.Genes) != len(parentX.Genes) {
		return false
	}
	for i := 0; i < len(child.Genes); i++ {
		if child.Genes[i] != parentX.Genes[i] && child.Genes[i] != parentY.Genes[i] {
			return false
		}
	}
	return true
}

func Test_GivenCrossover_WhenChildChanges_ThenParentsRemainUntouched(t *testing.T) {
	parentX := Individual{[]rune("abc")}
	parentY := Individual{[]rune("def")}

	genes := crossoverGenes(&parentX, &parentY, func(int random.IntType) bool { return true })
	genes[0] = rune('z')

	assert.Equal(t, []rune("abc"), parentX.Genes)
	assert.Equal(t, []rune("def"), parentY.Genes)
}

func TestMutationToMutateEveryGene(t *testing.T) {
	individual := Individual{[]rune("abc")}
	randomInt := func(maxValue int) int { return 1 }
	randomRune := func(runes []rune) rune { return rune('z') }
	runesPool := []rune("abc")

	individual.Mutate(1, randomInt, randomRune, runesPool)

	assert.Equal(t, []rune("zzz"), individual.Genes)
}

func Test_WhenRandomValueEqualsMutationRate_ThenDoNotMutate(t *testing.T) {
	randomInt := func(maxValue int) int { return 1 }
	assert.Equal(t, false, doesGeneMutate(randomInt, 0.01))
}

func Test_WhenRandomValueIsLowerThanMutationRate_ThenNotMutate(t *testing.T) {
	randomInt := func(maxValue int) int { return 1 }
	assert.Equal(t, true, doesGeneMutate(randomInt, 0.02))
}
