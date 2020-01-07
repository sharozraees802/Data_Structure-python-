using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Fibonacci_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 0;
            int n2 = 1;
            int n3,number,i;
            Console.Write("Enter a Number of Element:");
            number = Convert.ToInt32(Console.ReadLine());
            Console.Write(n+" "+n2+" ");

            for ( i =2 ; i <=number; i++)
            {
                n3 = n + n2;
                n = n2;
                n2 = n3;
                Console.Write(n3+" ");
            }
            Console.ReadLine();
        }
    }
}
