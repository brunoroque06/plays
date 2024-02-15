namespace Genetic;

public interface ITime : IGrainWithStringKey
{
    Task Elapse();
}
