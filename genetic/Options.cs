namespace Genetic;

public record Options(
    int MaxGenerations,
    int ReportInterval,
    int PopulationSize,
    float Elitism,
    float MutationRate,
    string TargetGenes,
    string Pool
);