using System.Text;

namespace Genetic;

public class Stochastic(Random random)
{
    public bool NextBool()
    {
        return random.Next(0, 2) == 0;
    }

    public int NextInt(int min, int max)
    {
        return random.Next(min, max);
    }

    public char NextChar(string pool)
    {
        return pool[random.Next(0, pool.Length)];
    }

    public string NextString(string pool, int length)
    {
        var str = new StringBuilder(length);

        foreach (var _ in Enumerable.Range(0, length))
            str.Append(pool[random.Next(0, pool.Length)]);

        return str.ToString();
    }
}
