using Microsoft.Extensions.Logging;

namespace Genetic;

public sealed class Reporter(ILogger<Reporter> logger) : Grain, IReporter
{
    public Task ReportGeneration(int generation, float fitness, string genes)
    {
        logger.LogInformation(
            "{{ \"Generation\": {gen,4}, \"Fitness\": {fit,0:0.00}, \"Genes\": \"{gen}\" }}",
            generation,
            fitness,
            genes
        );
        return Task.CompletedTask;
    }
}
