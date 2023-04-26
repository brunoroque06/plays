using Orleans.Concurrency;

namespace Genetic;

public interface IReporter : IGrainWithIntegerKey
{
    [OneWay]
    Task ReportGeneration(int generation, float fitness, string genes);
}
