using System.Text;

namespace Genetic;

public class Stochastic
{
    private readonly Random _random;

    public Stochastic(Random random)
    {
        _random = random;
    }

    public string NextString(string pool, int length)
    {
        var str = new StringBuilder(length);

        foreach (var _ in Enumerable.Range(0, length))
        {
            str.Append(pool[_random.Next(0, pool.Length)]);
        }

        return str.ToString();
    }
}
