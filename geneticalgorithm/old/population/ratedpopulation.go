package population

import (
	"errors"

	"github.com/brunoroque06/geneticalgorithm/individual"
	"github.com/brunoroque06/geneticalgorithm/random"
)

type RatedPopulation struct {
	BestGenes        []rune
	MaxFitness       float32
	fitnessSum       float32
	RatedIndividuals []*individual.RatedIndividual
}

func (ratedPopulation *RatedPopulation) findBestCouple() (int, int, error) {
	if len(ratedPopulation.RatedIndividuals) == 0 {
		return -1, -1, errors.New("population has no individuals")
	}
	best := 0
	secondBest := len(ratedPopulation.RatedIndividuals) - 1
	for i, ratedIndividual := range ratedPopulation.RatedIndividuals {
		if ratedPopulation.RatedIndividuals[best].Fitness < ratedIndividual.Fitness {
			secondBest = best
			best = i
		} else if ratedPopulation.RatedIndividuals[secondBest].Fitness < ratedIndividual.Fitness {
			secondBest = i
		}
	}
	return best, secondBest, nil
}

func (ratedPopulation *RatedPopulation) CreateNextGeneration(elitism float32, mutationRate float32, crossover individual.CrossoverType, randomBool random.BoolType, randomInt random.IntType, runesPool []rune) (*Population, error) {
	matingPool, matingPoolError := NewMatingPool(ratedPopulation)
	if len(ratedPopulation.RatedIndividuals) < 2 || matingPoolError != nil {
		return nil, errors.New("next generation could not be created")
	}
	nextGenerationIndividuals := make([]*individual.Individual, len(ratedPopulation.RatedIndividuals))
	numberElitismChilds := int(float32(len(ratedPopulation.RatedIndividuals)) * elitism)
	best, secondBest, _ := ratedPopulation.findBestCouple()
	for i := 0; i < len(nextGenerationIndividuals); i++ {
		if i < numberElitismChilds {
			nextGenerationIndividuals[i], _ = crossover(ratedPopulation.RatedIndividuals[best].Individual, ratedPopulation.RatedIndividuals[secondBest].Individual, randomBool)
		} else {
			parentX := matingPool.getRandomIndividual(randomInt)
			parentY := matingPool.getRandomIndividual(randomInt)
			nextGenerationIndividuals[i], _ = crossover(ratedPopulation.RatedIndividuals[parentX].Individual, ratedPopulation.RatedIndividuals[parentY].Individual, randomBool)
		}
		nextGenerationIndividuals[i].Mutate(mutationRate, randomInt, random.Rune, runesPool)
	}
	return &Population{nextGenerationIndividuals}, nil
}
