package individual

import (
	"errors"
	"github.com/brunoroque06/geneticalgorithm/random"
)

type (
	Individual struct {
		Genes []rune
	}
	CrossoverType func(parentX *Individual, parentY *Individual, randomBool random.BoolType) (*Individual, error)
)

func NewRandomIndividual(genesLen int, runesPool []rune, randomRunes random.RunesType) *Individual {
	genes := randomRunes(genesLen, runesPool)
	return &Individual{genes}
}

func NewRandomIndividuals(genesLen int, runesPool []rune, randomRunes random.RunesType, numberOfIndividuals int) []*Individual {
	individuals := make([]*Individual, numberOfIndividuals)
	for i := 0; i < len(individuals); i++ {
		individuals[i] = NewRandomIndividual(genesLen, runesPool, randomRunes)
	}
	return individuals
}

func (individual *Individual) EstimateFitness(target []rune) (float32, error) {
	if len(individual.Genes) != len(target) {
		return -1, errors.New("genes have different lengths")
	}
	return individual.estimateFitness(target), nil
}

func (individual *Individual) estimateFitness(target []rune) float32 {
	score := 0
	for i := 0; i < len(target); i++ {
		if target[i] == individual.Genes[i] {
			score++
		}
	}
	return float32(score) / float32(len(target))
}

func Crossover(parentX *Individual, parentY *Individual, randomBool random.BoolType) (*Individual, error) {
	if len(parentX.Genes) != len(parentY.Genes) {
		return nil, errors.New("parents do not have the same genes length")
	}
	return &Individual{crossoverGenes(parentX, parentY, randomBool)}, nil
}

func crossoverGenes(parentX *Individual, parentY *Individual, randomBool random.BoolType) []rune {
	childGenes := make([]rune, len(parentX.Genes))
	copy(childGenes, parentX.Genes)
	for i := 0; i < len(parentX.Genes); i++ {
		if randomBool(random.Int) {
			childGenes[i] = parentY.Genes[i]
		}
	}
	return childGenes
}

func (individual *Individual) Mutate(rate float32, randomInt random.IntType, randomGene random.RuneType, runesPool []rune) *Individual {
	for i := 0; i < len(individual.Genes); i++ {
		if doesGeneMutate(randomInt, rate) {
			individual.Genes[i] = randomGene(runesPool)
		}
	}
	return individual
}

func doesGeneMutate(randomInt random.IntType, rate float32) bool {
	randomValue := float32(randomInt(100)) / 100
	return randomValue < rate
}
