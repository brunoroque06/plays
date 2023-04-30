namespace Genetic;

public interface IGenetics : IGrainWithIntegerKey
{
    Task<Individual> GetIndividual();
    Task<bool> IsMaxFitness(Individual individual);
    Task<(Individual, Individual)[]> MatchParents(Individual[] individuals);
    Task Breed((Individual, Individual) parents);
}
