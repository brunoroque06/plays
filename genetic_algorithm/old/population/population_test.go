package population

import (
	"testing"

	"github.com/brunoroque06/geneticalgorithm/individual"
	"github.com/stretchr/testify/assert"
)

func Test_GivenPopulationWith1Gene_WhenRatingAgainst2Genes_ThenError(t *testing.T) {
	individuals := []*individual.Individual{{Genes: []rune("a")}}
	population := NewPopulation(individuals)
	target := []rune("ab")

	_, err := population.Rate(target)

	assert.NotNil(t, err)
}

func TestRatingPopulation(t *testing.T) {
	bestIndividual := individual.Individual{Genes: []rune("abcd")}
	ind := individual.Individual{Genes: []rune("efgh")}
	individuals := []*individual.Individual{&bestIndividual, &ind}
	population := NewPopulation(individuals)
	target := []rune("abch")

	ratedPopulation, err := population.Rate(target)

	assert.Equal(t, float32(0.75), ratedPopulation.MaxFitness)
	assert.Equal(t, float32(1), ratedPopulation.fitnessSum)
	assert.Equal(t, bestIndividual.Genes, ratedPopulation.BestGenes)
	assert.Equal(t, float32(0.75), ratedPopulation.RatedIndividuals[0].Fitness)
	assert.Equal(t, bestIndividual.Genes, ratedPopulation.RatedIndividuals[0].Individual.Genes)
	assert.Equal(t, float32(0.25), ratedPopulation.RatedIndividuals[1].Fitness)
	assert.Equal(t, ind.Genes, ratedPopulation.RatedIndividuals[1].Individual.Genes)
	assert.Nil(t, err)
}
