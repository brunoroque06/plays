package main

import (
	"log"
	"time"

	"github.com/brunoroque06/geneticalgorithm/individual"
	"github.com/brunoroque06/geneticalgorithm/population"
	"github.com/brunoroque06/geneticalgorithm/random"
)

func main() {
	random.Init()
	start := time.Now()
	target := "To be or not to be, that is the question."
	targetRunes := []rune(target)
	runesPool := []rune("abcdefghijklmnopqrstuvxz ,.T")
	individuals := individual.NewRandomIndividuals(len(target), runesPool, random.Runes, 100)
	pop := population.NewPopulation(individuals)
	ratedPopulation, _ := pop.Rate(targetRunes)
	generationNumber := 0
	for ratedPopulation.MaxFitness < 1 {
		pop, _ := ratedPopulation.CreateNextGeneration(0.25, 0.03, individual.Crossover, random.Bool, random.Int, runesPool)
		ratedPopulation, _ = pop.Rate(targetRunes)
		if generationNumber%25 == 0 {
			printStatistics(generationNumber, ratedPopulation.MaxFitness, string(ratedPopulation.BestGenes))
		}
		generationNumber++
	}
	printStatistics(generationNumber, ratedPopulation.MaxFitness, string(ratedPopulation.BestGenes))
	elapsed := time.Since(start)
	log.Printf("Elapsed time: %s", elapsed)
}

func printStatistics(generationNumber int, maxFitness float32, bestGenes string) {
	log.Printf("Generation: %4d | MaxFitness: %.3f | BestGenes: %v", generationNumber, maxFitness, bestGenes)
}
