using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace sir_zubair
{
    class Program
    {
        public class Node
        {
            public int value;
            public Node next;


        }

        public class MeriList
        {

            public Node start;
            public Node current;

            public int get(int index)
            {

                current = start;
                for (int i  = 0; i  <(index+1); i ++)
                {
                    if (current.next==null)
                    {
                        Console.WriteLine("get value: " + index);
                        break;
                    }
                    else
                    {
                        current = current.next;
                    }

                    
                }
                return current.value;
            }

            public void Add(int value)
            {

                if (start == null)
                {
                    start = new Node();
                    current = start;
                    current.value = value;
                }
                else
                {
                    while (true)
                    {
                        if (current.next == null)
                        {
                            current.next = new Node();
                            current = current.next;
                            current.value = value;
                            Console.WriteLine("insert value: " + value);
                            break;
                        }

                        else
                        {
                            current = current.next;
                        }
                        
                    }
                }
            }

        }

        static void Main(string[] args)
        {

            MeriList meri = new MeriList();
            meri.Add(25);
            meri.Add(23);
            meri.get(25);

        }
    }
}
