using NUnit.Framework;

namespace oop_limitations
{
    public class EncapsulationTests
    {
        [Test]
        public void ShouldBeSafe()
        {
            var core = new Kernel { Secret = 22 };

            var shell = new Shell(core);
            Assert.AreEqual(22, shell.Kernel.Secret, 0);

            core.Secret = 18;
            Assert.AreEqual(18, shell.Kernel.Secret, 0);
        }
    }
}
