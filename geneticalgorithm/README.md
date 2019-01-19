# Genetic Algorithm

This project consists of a genetic algorithm (heuristic, stochastic) that, given a `set of genes` (a string), creates a population that converges to that set using Darwinian Principles.

## Algorithm Description

The first generation is obtained by randomising every individual, where each individual is characterized by its genes. Then for each individual its fitness is estimated through comparison of its genes and the target `set of genes`. Finally the next generation is created using individuals from the current generation; using methods of crossover, and mutation.

Fitness is again estimated, and the next generation is created. This process is repeated until the maximum number of generations is reached, or when at least one individual obtains the target `set of genes`.

## Input Parameters

- `Target Set of Genes`, string that at least one element of the population should obtain;
- `Population Size`, number of elements of the population;
- `Elitism`, rate of children that are obtained through the crossover of two of the best parents of a given generation.
- `Mutation Rate`, mutation rate of each gene after the crossover;
- `Maximum Number of Generations`, maximum number of generations that the population has to achieve the target string;

## Output

```bash
Generation #    0 | MaxFitness: 0.20 | BestGenes: dllkvnnxx,u, th .epltTdqdmTothubjjuoalovn
Generation #   25 | MaxFitness: 0.51 | BestGenes: lgllpz.,pnoj td beh thattnTothe.queftaons
Generation #   50 | MaxFitness: 0.78 | BestGenes: Tt cpu., noT to be, thattisuthe question.
Generation #   75 | MaxFitness: 0.88 | BestGenes: Tt bp or noo to be, thatmisuthe question.
Generation #  100 | MaxFitness: 0.93 | BestGenes: To be or noo to be, thatmisuthe question.
Generation #  125 | MaxFitness: 0.95 | BestGenes: To be or no  to be, thatmis the question.
Generation #  150 | MaxFitness: 0.98 | BestGenes: To be or not to be, thatmis the question.
Generation #  175 | MaxFitness: 0.98 | BestGenes: To be or not to be, thatmis the question.
Generation #  192 | MaxFitness: 1.00 | BestGenes: To be or not to be, that is the question.
Elapsed time: 72.40605ms
```
