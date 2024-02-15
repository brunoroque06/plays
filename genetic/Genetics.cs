using System.Text;
using Orleans.Runtime;

namespace Genetic;

public class Genetics : Grain, IGenetics
{
    private readonly IPersistentState<Individual> _individual;
    private readonly Options _options;
    private readonly Stochastic _stochastic;

    public Genetics(
        [PersistentState("individual", "genetics")]
        IPersistentState<Individual> individual,
        Options options,
        Stochastic stochastic
    )
    {
        _individual = individual;
        _options = options;
        _stochastic = stochastic;
    }

    public Task<Individual> GetIndividual()
    {
        return Task.FromResult(_individual.State);
    }

    public Task<bool> IsMaxFitness(Individual individual)
    {
        return Task.FromResult(Math.Abs(individual.Fitness - 1.0f) < 1e-6);
    }

    public Task<(Individual, Individual)[]> MatchParents(Individual[] individuals)
    {
        var best = individuals.OrderByDescending(i => i.Fitness).Take(2).ToArray();

        var parents = new (Individual, Individual)[individuals.Length];
        var elite = (int) (individuals.Length * _options.Elitism);
        var pool = CreateMatingPool(individuals);
        foreach (var i in Enumerable.Range(0, individuals.Length))
            if (i < elite)
            {
                parents[i] = (best[0], best[1]);
            }
            else
            {
                var x = _stochastic.NextInt(0, pool.Length);
                var y = _stochastic.NextInt(0, pool.Length);
                parents[i] = (pool[x], pool[y]);
            }

        return Task.FromResult(parents);
    }

    public async Task Breed((Individual, Individual) parents)
    {
        var (x, y) = parents;
        var genes = new StringBuilder();

        foreach (var i in Enumerable.Range(0, x.Genes.Length))
            if (_stochastic.NextInt(0, 100) / 100.0 < _options.MutationRate)
                genes.Append(_stochastic.NextChar(_options.Pool));
            else if (_stochastic.NextBool())
                genes.Append(x.Genes[i]);
            else
                genes.Append(y.Genes[i]);

        await SaveIndividual(genes.ToString());
    }

    public override async Task OnActivateAsync(CancellationToken cancellationToken)
    {
        if (_individual.RecordExists)
        {
            await _individual.ReadStateAsync();
            return;
        }

        var genes = _stochastic.NextString(_options.Pool, _options.TargetGenes.Length);
        await SaveIndividual(genes);
    }

    private static float CalcFitness(string target, string genes)
    {
        var matches = Enumerable.Range(0, target.Length).Count(i => target[i].Equals(genes[i]));
        return (float) matches / target.Length;
    }

    private async Task SaveIndividual(string genes)
    {
        _individual.State = new Individual(genes, CalcFitness(_options.TargetGenes, genes));
        await _individual.WriteStateAsync();
    }

    private static Individual[] CreateMatingPool(Individual[] individuals)
    {
        var sum = individuals.Select(i => i.Fitness).Sum();
        var pool = new List<Individual>();

        foreach (var ind in individuals)
        {
            var weight = (int) (ind.Fitness / sum * individuals.Length * 2);
            pool.AddRange(Enumerable.Repeat(ind, weight));
        }

        return pool.ToArray();
    }
}