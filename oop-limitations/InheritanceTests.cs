using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace OopLimitations
{
    [TestClass]
    public class InheritanceTests
    {
        [TestMethod]
        public void JustWantTheBanana()
        {
            Console.WriteLine(new Banana {Trees = 999, Fur = 1234, Calories = 89});
        }
    }
}