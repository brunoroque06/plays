namespace Genetic;

public sealed record Options(
    int MaxGenerations,
    int ReportInterval,
    int PopulationSize,
    float Elitism,
    float MutationRate,
    string TargetGenes,
    string Pool
);
