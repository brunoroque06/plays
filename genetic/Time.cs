namespace Genetic;

public sealed class Time(IGrainFactory client, Options options) : Grain, ITime
{
    public async Task Elapse()
    {
        foreach (var gen in Enumerable.Range(0, options.MaxGenerations))
        {
            var individuals = await Task.WhenAll(
                Enumerable
                    .Range(0, options.PopulationSize)
                    .Select(i => client.GetGrain<IGenetics>(i).GetIndividual())
            );

            var fitness = individuals.Select(i => i.Fitness).ToArray();
            var maxFitness = fitness.Max();
            var fittest = individuals[Array.IndexOf(fitness, maxFitness)];
            var isMaxFitness = await client.GetGrain<IGenetics>(0).IsMaxFitness(fittest);

            var last = isMaxFitness || gen == options.MaxGenerations - 1;

            if (gen % options.ReportInterval == 0 || last)
                await client
                    .GetGrain<IReporter>(0)
                    .ReportGeneration(gen, maxFitness, fittest.Genes);

            if (last)
                return;

            var parents = await client.GetGrain<IGenetics>(0).MatchParents(individuals);

            await Task.WhenAll(
                parents
                    .Zip(
                        Enumerable
                            .Range(0, parents.Length)
                            .Select(i => client.GetGrain<IGenetics>(i))
                    )
                    .Select(z => z.Second.Breed(z.First))
            );
        }
    }
}
