using System.Text;
using Orleans.Runtime;

namespace Genetic;

public class Genetics(
    [PersistentState("individual", "genetics")] IPersistentState<Individual> individual,
    Options options,
    Stochastic stochastic
) : Grain, IGenetics
{
    public Task<Individual> GetIndividual()
    {
        return Task.FromResult(individual.State);
    }

    public Task<bool> IsMaxFitness(Individual individual)
    {
        return Task.FromResult(Math.Abs(individual.Fitness - 1.0f) < 1e-6);
    }

    public Task<(Individual, Individual)[]> MatchParents(Individual[] individuals)
    {
        var best = individuals.OrderByDescending(i => i.Fitness).Take(2).ToArray();

        var parents = new (Individual, Individual)[individuals.Length];
        var elite = (int)(individuals.Length * options.Elitism);
        var pool = CreateMatingPool(individuals);
        foreach (var i in Enumerable.Range(0, individuals.Length))
            if (i < elite)
            {
                parents[i] = (best[0], best[1]);
            }
            else
            {
                var x = stochastic.NextInt(0, pool.Length);
                var y = stochastic.NextInt(0, pool.Length);
                parents[i] = (pool[x], pool[y]);
            }

        return Task.FromResult(parents);
    }

    public async Task Breed((Individual, Individual) parents)
    {
        var (x, y) = parents;
        var genes = new StringBuilder();

        foreach (var i in Enumerable.Range(0, x.Genes.Length))
            if (stochastic.NextInt(0, 100) / 100.0 < options.MutationRate)
                genes.Append(stochastic.NextChar(options.Pool));
            else if (stochastic.NextBool())
                genes.Append(x.Genes[i]);
            else
                genes.Append(y.Genes[i]);

        await SaveIndividual(genes.ToString());
    }

    public override async Task OnActivateAsync(CancellationToken cancellationToken)
    {
        if (individual.RecordExists)
        {
            await individual.ReadStateAsync();
            return;
        }

        var genes = stochastic.NextString(options.Pool, options.TargetGenes.Length);
        await SaveIndividual(genes);
    }

    private static float CalcFitness(string target, string genes)
    {
        var matches = Enumerable.Range(0, target.Length).Count(i => target[i].Equals(genes[i]));
        return (float)matches / target.Length;
    }

    private async Task SaveIndividual(string genes)
    {
        individual.State = new Individual(genes, CalcFitness(options.TargetGenes, genes));
        await individual.WriteStateAsync();
    }

    private static Individual[] CreateMatingPool(Individual[] individuals)
    {
        var sum = individuals.Select(i => i.Fitness).Sum();
        var pool = new List<Individual>();

        foreach (var ind in individuals)
        {
            var weight = (int)(ind.Fitness / sum * individuals.Length * 2);
            pool.AddRange(Enumerable.Repeat(ind, weight));
        }

        return pool.ToArray();
    }
}
