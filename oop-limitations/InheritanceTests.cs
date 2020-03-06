using System;
using NUnit.Framework;

namespace oop_limitations
{
    public class InheritanceTests
    {
        [Test]
        public void JustWantTheBanana()
        {
            Console.WriteLine(new Banana { Trees = 999, Fur = 1234, Calories = 89 });
        }
    }
}