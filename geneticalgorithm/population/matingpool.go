package population

import (
	"errors"
	"github.com/brunoroque06/geneticalgorithm/random"
)

type (
	MatingPool struct {
		individualsByFitness []int
	}
)

func NewMatingPool(ratedPopulation *RatedPopulation) (*MatingPool, error) {
	if len(ratedPopulation.RatedIndividuals) == 0 {
		return nil, errors.New("population must have at least 1 individual")
	} else {
		pool := estimatePool(ratedPopulation)
		return &MatingPool{pool}, nil
	}
}

func estimatePool(ratedPopulation *RatedPopulation) []int {
	var pool []int
	for i, ind := range ratedPopulation.RatedIndividuals {
		numberOfTimes := estimateNumberOfTimes(ind.Fitness, ratedPopulation.fitnessSum, len(ratedPopulation.RatedIndividuals))
		for j := 0; j < numberOfTimes; j++ {
			pool = append(pool, i)
		}
	}
	return pool
}

func estimateNumberOfTimes(fitness float32, fitnessSum float32, numberOfIndividuals int) int {
	return int(fitness / fitnessSum * float32(numberOfIndividuals) * 2)
}

func (matingPool *MatingPool) getRandomIndividual(random random.IntType) int {
	return matingPool.individualsByFitness[random(len(matingPool.individualsByFitness)-1)]
}
