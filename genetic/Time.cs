namespace Genetic;

public class Time : Grain, ITime
{
    private readonly IClusterClient _client;
    private readonly Options _options;

    public Time(IClusterClient client, Options options)
    {
        _client = client;
        _options = options;
    }

    public async Task Elapse()
    {
        foreach (var gen in Enumerable.Range(0, _options.MaxGenerations))
        {
            var individuals = await Task.WhenAll(
                Enumerable
                    .Range(0, _options.PopulationSize)
                    .Select(i => _client.GetGrain<IGenetics>(i).GetIndividual())
            );

            var fitness = individuals.Select(i => i.Fitness).ToArray();
            var maxFitness = fitness.Max();
            var fittest = individuals[Array.IndexOf(fitness, maxFitness)];
            var isMaxFitness = await _client.GetGrain<IGenetics>(0).IsMaxFitness(fittest);

            var last = isMaxFitness || gen == _options.MaxGenerations;

            if (gen % _options.ReportInterval == 0 || last)
                await _client
                    .GetGrain<IReporter>(0)
                    .ReportGeneration(gen, maxFitness, fittest.Genes);

            if (last)
                return;

            var parents = await _client.GetGrain<IGenetics>(0).MatchParents(individuals);

            await Task.WhenAll(
                parents
                    .Zip(
                        Enumerable
                            .Range(0, parents.Length)
                            .Select(i => _client.GetGrain<IGenetics>(i))
                    )
                    .Select(z => z.Second.Breed(z.First))
            );
        }
    }
}
