using Orleans.Runtime;

namespace Genetic;

public class Genetics : Grain, IGenetics
{
    private readonly IPersistentState<Individual> _individual;
    private readonly Options _options;
    private readonly Stochastic _stochastic;

    public Genetics(
        [PersistentState("individual", "genetics")] IPersistentState<Individual> individual,
        Options options,
        Stochastic stochastic
    )
    {
        _individual = individual;
        _options = options;
        _stochastic = stochastic;
    }

    public override async Task OnActivateAsync(CancellationToken cancellationToken)
    {
        if (_individual.RecordExists)
        {
            await _individual.ReadStateAsync();
            return;
        }

        var genes = _stochastic.NextString(_options.Pool, _options.TargetGenes.Length);
        _individual.State = new Individual(genes, CalcFitness(_options.TargetGenes, genes));
        await _individual.WriteStateAsync();
    }

    private static float CalcFitness(string target, string genes)
    {
        var matches = Enumerable.Range(0, target.Length).Count(i => target[i].Equals(genes[i]));
        return (float)matches / target.Length;
    }

    public Task<Individual> GetIndividual()
    {
        return Task.FromResult(_individual.State);
    }

    public Task Something()
    {
        return Task.CompletedTask;
    }
}
