//Hello
//My first C# code.

using System;
using System.Threading;

class Program
{
  static void Main(string[] args)
  {
    Console.Clear();
    Console.Title = "Hello";
    Console.WriteLine("Hello there, what is your name?");
    string name = Console.ReadLine();
    Console.WriteLine("");
    Console.WriteLine("Nice to meet you, {0}.", name);
    Console.WriteLine("");
    Console.WriteLine("How old are you?");
    int age = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("");
    if (age >= 18)
    {
      Console.WriteLine("Don't get yourself in trouble, okay?");
    }
    else if (age < 18)
    {
      Console.WriteLine("Having fun?");
    }
    Console.WriteLine("Well, i have to go now, bye!");
    Thread.Sleep(3);
    Console.Clear();
  }
}
