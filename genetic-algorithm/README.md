# Genetic Algorithm

This project consists of a genetic algorithm (heuristic, stochastic) that, given a `set of genes`, creates a population that converges to that set using Darwinian Principles.

## Algorithm Description

The first generation is obtained by randomising every individual, where each individual is characterized by its genes. Then for each individual its fitness is estimated through comparison of its genes and the target `set of genes`. The next generation is then created using individuals from the current generation, by using methods of crossover and mutation. Fitness is again estimated, and the next generation is created. This process is repeated until the maximum number of generations is reached, or when at least one individual obtains the target `set of genes`.

Crossover consists of the combination of any 2 individuals of a given generation. An individual is more likely to be picked from the mating pool the higher its fitness is. Crossover works on combining the good genes already in the population. Mutation changes genes randomly of a given individual, and is a method used to bring new genes into the population.

## Input Parameters

- `Target Set of Genes`, string that at least one element of the population should obtain;
- `Population Size`, number of elements of the population;
- `Elitism`, rate of children that are obtained through the crossover of two of the best parents of a given generation.
- `Mutation Rate`, mutation rate of each gene after the crossover;
- `Maximum Number of Generations`, maximum number of generations that the population has to achieve the target string;

## Output Example

```shell
Gen Fit  Genes
010 0.41 ncibebkd ncq tf oee fhecpzsxtru uTeotibn.
020 0.51 novbe bd noq tf oee fheupzsxthu uTeotibn.
030 0.59 novbe bd noq tr oe, fhecpisxthu uTeotisn.
040 0.66 no be bd noq te oe, thacpistthu i eotion.
050 0.73 no be br noq te oe, thacpistthu q estion.
060 0.80 no be br noq te be, thatpistthe q estion.
070 0.90 no be br not te be, that istthe question.
080 0.88 no be br not te be, that istthe question.
090 0.95 no be br not to be, that is the question.
100 0.98 no be or not to be, that is the question.
110 0.98 no be or not to be, that is the question.
120 0.98 no be or not to be, that is the question.
123 1.00 To be or not to be, that is the question.
```
