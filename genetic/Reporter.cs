using Microsoft.Extensions.Logging;

namespace Genetic;

public class Reporter : Grain, IReporter
{
    private readonly ILogger<Reporter> _logger;

    public Reporter(ILogger<Reporter> logger)
    {
        _logger = logger;
    }

    public Task ReportGeneration(int generation, float fitness, string genes)
    {
        _logger.LogInformation(
            "{{ \"Generation\": {gen,4}, \"Fitness\": {fit,0:0.00}, \"Genes\": \"{gen}\" }}",
            generation,
            fitness,
            genes
        );
        return Task.CompletedTask;
    }
}
