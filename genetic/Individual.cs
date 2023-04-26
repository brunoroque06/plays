namespace Genetic;

[GenerateSerializer]
public record Individual(string Genes, float Fitness)
{
    public Individual()
        : this(string.Empty, 0) { }
}
