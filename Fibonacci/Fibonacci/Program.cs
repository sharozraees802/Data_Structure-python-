using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Fibonacci
{
    class Program
    {
        static void Main(string[] args)
        {

         

            int n1 = 0, n2 = 1, n3, i, number;
            Console.Write("Enter the number of elements: ");
            number = int.Parse(Console.ReadLine());
            int[] arr1 = new int[number + 5];
            int[] arr2 = new int[number + 5];
            int[] finalstate11 = new int[number + 5];
            for (int q = 0; q < (number + 5); q++)
            {
                arr1[q] = 0; arr2[q] = 0; finalstate11[q] = 0;
            }

            Console.Write("\nFab Series : ");
            Console.Write(n1 + " " + n2 + " ");
            arr1[0] = number;
            arr1[1] = n1;
            arr1[2] = n2;
            int counter = 3;
            for (i = 2; i < number; ++i)
            {
                n3 = n1 + n2;
                if (n3 <= number && n3 > 0)
                {
                    Console.Write(n3 + " ");
                    arr1[counter++] = n3;
                }
                if (n3 == number)
                {
                    break;
                }
                n1 = n2;
                n2 = n3;
            }
            Console.Write("\n\nFab after inserting value : ");
            Console.Write(arr1[0] + " " + arr1[1] + " ");
            counter = 2;
            for (int y = 2; y < arr1.Length; y++)
            {
                if (arr1[y] == 0)
                {
                    break;
                }
                Console.Write(arr1[y] + " ");
                counter++;
            }

            ////////////
            // checking for prime number and 
            //and making final state here 
            // Name wise feel the differt
            for (int c = 0; c < counter; c++)
            {

                int m = 0, flag = 0;
                m = arr1[c] / 2;
                for (int j = 2; j <= m; j++)
                {
                    if (arr1[c] % j == 0)
                    {
                        finalstate11[c] = arr1[c];
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                {
                    if (arr1[c] >= 2)
                    {
                        arr2[c] = arr1[c];
                    }
                    else
                    {
                        finalstate11[c] = arr1[c];
                    }
                }
            }

            Console.Write("\n\n Prime numbers :");
            for (int y = 2; y < arr2.Length; y++)
            {
                if (arr2[y] == 0)
                {
                    continue;
                }

                Console.Write(arr2[y] + " ");
            }
            Console.WriteLine("\n\n After deleting prime numbers!!");
            Console.Write("Final State :");
            Console.Write(finalstate11[0] + " " + finalstate11[1] + " ");
            for (int y = 2; y < finalstate11.Length; y++)
            {
                if (finalstate11[y] == 0)
                {
                    continue;
                }

                Console.Write(finalstate11[y] + " ");
            }

            
        }
    }
}
