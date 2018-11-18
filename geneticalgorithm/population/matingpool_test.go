package population

import (
	"github.com/brunoroque06/geneticalgorithm/individual"
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_GivenPopulationHasNoIndividuals_WhenCreatingMatingPool_ThenError(t *testing.T) {
	ratedPopulation := &RatedPopulation{[]rune{}, 0, 0, []*individual.RatedIndividual{}}

	_, err := NewMatingPool(ratedPopulation)

	assert.NotNil(t, err)
}

func TestMatingPoolCreation(t *testing.T) {
	ratedIndividuals := []*individual.RatedIndividual{{&individual.Individual{}, 0.25}, {&individual.Individual{}, 0.50}, {&individual.Individual{}, 0.25}, {&individual.Individual{}, 0.75}}
	ratedPopulation := NewRatedPopulation(ratedIndividuals)

	pool, err := NewMatingPool(ratedPopulation)

	assert.Equal(t, []int{0, 1, 1, 2, 3, 3, 3}, pool.individualsByFitness)
	assert.Nil(t, err)
}
