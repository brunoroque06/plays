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
Generation:    0 | MaxFitness: 0.17 | BestGenes: epbzzxztknrvmth ectftmgearTrhce effTfa.nq
Generation:   25 | MaxFitness: 0.54 | BestGenes: Tplbztojknovbto reg,tsatifsghhe epestions
Generation:   50 | MaxFitness: 0.71 | BestGenes: To,betox notlto je utsat lsqhhe questions
Generation:   75 | MaxFitness: 0.76 | BestGenes: Tocbetox notkto je  tsat lsqthe questions
Generation:  100 | MaxFitness: 0.88 | BestGenes: Toxbe or not to je  that lscthe question.
Generation:  125 | MaxFitness: 0.95 | BestGenes: Toxbe or not to beh that is the question.
Generation:  150 | MaxFitness: 0.98 | BestGenes: To be or not to beb that is the question.
Generation:  166 | MaxFitness: 1.00 | BestGenes: To be or not to be, that is the question.
Elapsed time: 70.583113ms
```
