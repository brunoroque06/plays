namespace oop_limitations
{
    public class Kernel
    {
        public int Secret { get; set; }
    }

    public class Shell
    {
        public Kernel Kernel { get; }

        public Shell(Kernel kernel)
        {
            Kernel = kernel;
        }
    }
}