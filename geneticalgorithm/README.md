# Genetic Algorithm

This project consists of a genetic algorithm (heuristic, stochastic algorithm) that, given a target string (genes), creates a population that converges to that same string using Darwinian Principles.

## Algorithm Description

The first generation is obtained by randomising every individual, where each individual is characterized by its genes ([]rune).

Then for each individual its fitness is estimated, through comparison of its genes with the "target string".

Finally the next generation is created using individuals from the current generation using methods of crossover between 2 individuals, and mutation.

Fitness is again estimated, and a next generation is created. This process is repeated until the maximum number of generations is reached, or when at least one individual obtains the "target string".

## Inputs

Inputs are the following:

- `Target String`, string that at least one element of the population should obtain;
- `Population Size`, number of elements of the population;
- `Mutation Rate`, mutation rate of each gene;
- `Maximum Number of Generations`, maximum number of generations that the population has to guess the target string;
- `Elitism`, rate of children that are obtained through the crossover of two of the best parents of a given generation.

## Outputs

```bash
2018/11/18 03:42:41 Generation:    0 | MaxFitness: 0.195 | BestGenes: ipnedTn.suntftj,vq,mrxatevn kcfdqda.bxcz.
2018/11/18 03:42:41 Generation:   25 | MaxFitness: 0.610 | BestGenes: io e,Ton gTt tn,ve,zthateis tkeaquastiin.
2018/11/18 03:42:41 Generation:   50 | MaxFitness: 0.732 | BestGenes: io beTon not tj te,athatzis tkeaquastirn.
2018/11/18 03:42:41 Generation:   75 | MaxFitness: 0.805 | BestGenes: do beqor not to te,zthatais tde quastiln.
2018/11/18 03:42:41 Generation:  100 | MaxFitness: 0.854 | BestGenes: do beqor not to Te, thatsis tde quqstion.
2018/11/18 03:42:41 Generation:  125 | MaxFitness: 0.902 | BestGenes: po bevor not to se, thatxis the question.
2018/11/18 03:42:41 Generation:  150 | MaxFitness: 0.976 | BestGenes: To be or not to be, thatmis the question.
2018/11/18 03:42:41 Generation:  175 | MaxFitness: 0.976 | BestGenes: To be or not to be, thatcis the question.
2018/11/18 03:42:41 Generation:  194 | MaxFitness: 1.000 | BestGenes: To be or not to be, that is the question.
2018/11/18 03:42:41 Elapsed time: 69.034305ms
```
