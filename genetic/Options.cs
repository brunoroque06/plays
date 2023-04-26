namespace Genetic;

public record Options(
    int MaxGenerations,
    int PopulationSize,
    float Elitism,
    float MutationRate,
    string TargetGenes,
    string Pool
);
