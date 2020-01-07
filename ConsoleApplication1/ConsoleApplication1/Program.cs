using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Node
    {
        public int Info;
        public Node Left;
        public Node Right;

        public Node(int value)
        {
            Info = value;
            Left = null;
            Right = null;
        }
    }

    class BinaryTree
    {
        public Node Root;

        public BinaryTree()
        {
            Root = null;
        }

        public Node Highestvalue(Node ptr)
        {
            if (ptr.Right != null)
            {
                return Highestvalue(ptr.Right);
            }
            return ptr;
        }

        public Node Delete(Node ptr, int value)
        {
            if (ptr == null)
            {
                Console.WriteLine("Value Not Found");
                return null;
            }
            else if (value < ptr.Info) {
                ptr.Left = Delete(ptr.Left, value);
            }
            else if (value > ptr.Info)
            {
                ptr.Right = Delete(ptr.Right, value);
            }
            else {
                if (ptr.Left != null && ptr.Right != null)
                {
                    Node Temp = Highestvalue(ptr.Left);
                    ptr.Info = Temp.Info;
                    ptr.Left = Delete(ptr.Left, Temp.Info);

                }
                else if (ptr.Left == null)
                {
                    ptr = ptr.Right;
                }
                else if (ptr.Right == null)
                {
                    ptr = ptr.Left;
                }
            }
            return ptr;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
        }
    }
}
