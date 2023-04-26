namespace Genetic;

public interface IGenetics : IGrainWithIntegerKey
{
    Task<Individual> GetIndividual();
    Task Something();
}
