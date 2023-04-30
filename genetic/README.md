# Genetic Algorithm

This project consists of a genetic algorithm (heuristic, stochastic) that, given a target genes, creates a population that converges to that target using natural selection (Darwinism).

## Description

The first generation is obtained by randomising every individual, where each individual is characterized by its genes. Then for each individual, its fitness is estimated through comparison of its genes and the target genes. The next generation is then created using individuals from the current generation, by using methods of crossover and mutation. This process is repeated until the maximum number of generations is reached, or when at least one individual obtains the target genes.

Crossover consists of the combination of any 2 individuals of a given generation, thus combining genes already in the population. Individuals are picked to be parents based on their fitness (higher is better). Mutation changes genes randomly of a given individual; it is used to bring new genes into the population.

## Parameters

- `Target Genes`, genes that at least one element of the population should obtain;
- `Population Size`, number of individuals in the population;
- `Elitism`, rate of children that are obtained through the crossover of two of the best parents of a given generation;
- `Mutation Rate`, mutation rate of each gene after the crossover;
- `Number of Generations`, maximum number of generations that the population has to achieve the target genes.

## Example (Output)

```json
{ "Generation":   0, "Fitness": 0.15, "Genes": "ztvb,qtneermvnvnob,joqltnTd ,dehqphbrrkqT" }
{ "Generation":  10, "Fitness": 0.34, "Genes": "aznbojonen m ,o ld,jotlt i, ,hehqiaurqsft" }
{ "Generation":  20, "Fitness": 0.46, "Genes": "aznbojonenom ,o le,jotat iT ,hehqiastqsau" }
{ "Generation":  30, "Fitness": 0.54, "Genes": "adnbujonenom ,o be,jotat iT ,he quastqsau" }
{ "Generation":  40, "Fitness": 0.56, "Genes": "adnbu onenom ,o be,jotat iT ,he quastdsau" }
{ "Generation":  50, "Fitness": 0.63, "Genes": "adnbf onbnot ,o be,jotat iT ,he quastdan." }
{ "Generation":  60, "Fitness": 0.71, "Genes": "aonbf onbnot to be,jotat iT ,he quastdon." }
{ "Generation":  70, "Fitness": 0.78, "Genes": " onbf or not to be,jo.at iT the quastdon." }
{ "Generation":  80, "Fitness": 0.80, "Genes": "oonbf or not to be,jo.at iT the questdon." }
{ "Generation":  90, "Fitness": 0.88, "Genes": "oonbe or not to be,jt.at is the questdon." }
{ "Generation": 110, "Fitness": 0.93, "Genes": "Tonbe or not to be,jt.at is the question." }
{ "Generation": 120, "Fitness": 0.95, "Genes": "Tonbe or not to be, t.at is the question." }
{ "Generation": 130, "Fitness": 0.98, "Genes": "To be or not to be, t.at is the question." }
{ "Generation": 140, "Fitness": 0.98, "Genes": "To be or not to be, tlat is the question." }
{ "Generation": 150, "Fitness": 0.98, "Genes": "To be or not to be, tlat is the question." }
{ "Generation": 160, "Fitness": 0.98, "Genes": "To be or not to be, tlat is the question." }
{ "Generation": 162, "Fitness": 1.00, "Genes": "To be or not to be, that is the question." }
```
