namespace Genetic;

[GenerateSerializer]
public sealed record Individual(string Genes, float Fitness)
{
    public Individual()
        : this(string.Empty, 0) { }
}
