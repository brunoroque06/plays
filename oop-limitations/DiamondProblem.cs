using System;

namespace OopLimitations
{
    public class Device
    {
        public virtual void Power()
        {
            Console.WriteLine("Powering device");
        }
    }

    public class Phone : Device
    {
        public override void Power()
        {
            Console.WriteLine("Powering phone");
        }
    }

    public class Computer : Device
    {
        public override void Power()
        {
            Console.WriteLine("Powering computer");
        }
    }

    public class SmartPhone { } // : Phone, Computer

    public class SmartPhoneContainAndDelegate // Black Box -> White Box
    {
        private readonly Phone _phone;
        private readonly Computer _computer;

        public SmartPhoneContainAndDelegate(Phone phone, Computer computer)
        {
            _phone = phone;
            _computer = computer;
        }

        public void Power()
        {
            // Which implementation to use?
            _phone.Power();
            _computer.Power();
        }
    }
}