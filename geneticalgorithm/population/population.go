package population

import (
	"github.com/brunoroque06/geneticalgorithm/individual"
)

type Population struct {
	individuals []*individual.Individual
}

func NewPopulation(individuals []*individual.Individual) *Population {
	return &Population{individuals}
}

func (population *Population) Rate(target []rune) (RatedPopulation, error) {
	maxFitness := float32(0)
	fitnessSum := float32(0)
	bestGenes := []rune("")
	var err error = nil
	ratedIndividuals := make([]*individual.RatedIndividual, len(population.individuals))
	for i, ind := range population.individuals {
		fitness, er := ind.EstimateFitness(target)
		if er != nil {
			err = er
			break
		}
		if fitness > maxFitness {
			maxFitness = fitness
			bestGenes = ind.Genes
		}
		fitnessSum += fitness
		ratedIndividuals[i] = &individual.RatedIndividual{Individual: ind, Fitness: fitness}
	}
	return RatedPopulation{bestGenes, maxFitness, fitnessSum, ratedIndividuals}, err
}
