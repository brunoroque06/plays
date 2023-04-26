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

            if (gen % 10 == 0)
            {
                var maxFitnessInd = Array.IndexOf(fitness, maxFitness);
                await _client
                    .GetGrain<IReporter>(0)
                    .ReportGeneration(gen, maxFitness, individuals[maxFitnessInd].Genes);
            }

            if (Math.Abs(maxFitness - 1.0f) < 1e-10 || gen == _options.MaxGenerations)
                return;
        }
    }
}
