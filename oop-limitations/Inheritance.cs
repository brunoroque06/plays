namespace OopLimitations
{
    public class Jungle
    {
        public int Trees { get; set; }
    }
    public class Gorilla : Jungle
    {
        public int Fur { get; set; }
    }

    public class Banana : Gorilla
    {
        public int Calories { get; set; }
    }
}