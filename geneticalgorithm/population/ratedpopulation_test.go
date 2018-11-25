package population

import (
	"testing"

	"github.com/brunoroque06/geneticalgorithm/individual"
	"github.com/brunoroque06/geneticalgorithm/random"
	"github.com/stretchr/testify/assert"
)

func NewRatedPopulation(ratedIndividuals []*individual.RatedIndividual) *RatedPopulation {
	maxFitness := float32(0)
	fitnessSum := float32(0)
	bestGenes := ratedIndividuals[0].Individual.Genes
	for _, ratedI := range ratedIndividuals {
		fitnessSum += ratedI.Fitness
		if maxFitness < ratedI.Fitness {
			maxFitness = ratedI.Fitness
			bestGenes = ratedI.Individual.Genes
		}
	}
	return &RatedPopulation{bestGenes, maxFitness, fitnessSum, ratedIndividuals}
}

func TestRandomPopulationCreation(t *testing.T) {
	bestGenes := []rune("b")
	ratedIndividuals := []*individual.RatedIndividual{{&individual.Individual{[]rune("a")}, 0.25}, {&individual.Individual{bestGenes}, 0.75}, {&individual.Individual{[]rune("c")}, 0.60}}

	ratedPopulation := NewRatedPopulation(ratedIndividuals)

	assert.Equal(t, float32(1.6), ratedPopulation.fitnessSum)
	assert.Equal(t, float32(0.75), ratedPopulation.MaxFitness)
	assert.Equal(t, bestGenes, ratedPopulation.BestGenes)
	assert.Equal(t, ratedIndividuals, ratedPopulation.RatedIndividuals)
}

func Test_GivenNoIndividuals_WhenFindBestCouple_ThenError(t *testing.T) {
	ratedPopulation := RatedPopulation{[]rune{}, 0, 0, []*individual.RatedIndividual{}}

	best, secondBest, err := ratedPopulation.findBestCouple()

	assert.Equal(t, -1, best)
	assert.Equal(t, -1, secondBest)
	assert.NotNil(t, err)
}

func Test_GivenIndividualsWithDifferentFitnessValues_WhenFindBestCouple_ThenFindTheBestTwo(t *testing.T) {
	ratedIndividuals := []*individual.RatedIndividual{{&individual.Individual{}, 0.50}, {&individual.Individual{}, 0.25}, {&individual.Individual{}, 0.75}, {&individual.Individual{}, 0.60}}
	ratedPopulation := NewRatedPopulation(ratedIndividuals)

	best, secondBest, err := ratedPopulation.findBestCouple()

	assert.Equal(t, 2, best)
	assert.Equal(t, 3, secondBest)
	assert.Nil(t, err)
}

func Test_GivenIndividualsWithEqualFitnessValues_WhenFindBestCouple_ThenFirstAndLast(t *testing.T) {
	ratedIndividuals := []*individual.RatedIndividual{{&individual.Individual{}, 0.50}, {&individual.Individual{}, 0.50}, {&individual.Individual{}, 0.50}}
	ratedPopulation := NewRatedPopulation(ratedIndividuals)

	best, secondBest, err := ratedPopulation.findBestCouple()

	assert.Equal(t, 0, best)
	assert.Equal(t, 2, secondBest)
	assert.Nil(t, err)
}

func TestNextGenerationToNeedAtLeastTwoIndividuals(t *testing.T) {
	ratedPopulation := RatedPopulation{[]rune{}, 0, 0, []*individual.RatedIndividual{}}
	crossover := func(parentX *individual.Individual, parentY *individual.Individual, randomBool random.BoolType) (*individual.Individual, error) {
		return nil, nil
	}
	randomBool := func(int random.IntType) bool { return true }
	randomInt := func(maxValue int) int { return 1 }

	_, err := ratedPopulation.CreateNextGeneration(0, 0, crossover, randomBool, randomInt, []rune(""))

	assert.NotNil(t, err)
}

func TestNextGenerationToConsistOfHalfChildrenFromTheBestCoupleAndHalfFromWorst(t *testing.T) {
	ratedIndividuals := []*individual.RatedIndividual{{&individual.Individual{}, 0.50}, {&individual.Individual{}, 0.25}, {&individual.Individual{}, 0.75}, {&individual.Individual{}, 0.60}}
	ratedPopulation := NewRatedPopulation(ratedIndividuals)
	bestCoupleChildGenes := []rune("best-genes")
	crossover := func(parentX *individual.Individual, parentY *individual.Individual, randomBool random.BoolType) (*individual.Individual, error) {
		return &individual.Individual{Genes: bestCoupleChildGenes}, nil
	}
	randomBool := func(int random.IntType) bool { return true }
	randomInt := func(maxValue int) int { return 1 }

	population, error := ratedPopulation.CreateNextGeneration(0.5, 0, crossover, randomBool, randomInt, []rune(""))

	assert.Equal(t, 4, len(population.individuals))
	assert.Equal(t, bestCoupleChildGenes, population.individuals[0].Genes)
	assert.Equal(t, bestCoupleChildGenes, population.individuals[1].Genes)
	assert.Equal(t, bestCoupleChildGenes, population.individuals[2].Genes)
	assert.Equal(t, bestCoupleChildGenes, population.individuals[3].Genes)
	assert.Nil(t, error)
}
