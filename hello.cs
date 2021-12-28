//Hello
//My first C# program.

using System;
using System.Threading;

class Program
{
  static void Main(string[] args)
  {
    Console.Clear();
    Console.Title = "Hello";
    Console.WriteLine("Hello there, what is your name?");
    string user_name = Console.ReadLine();
    Console.WriteLine("");
    Console.WriteLine("Nice to meet you, {0}.", user_name);
    Console.WriteLine("");
    Console.WriteLine("How old are you?");
    int user_age = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("");
    if (user_age >= 18)
    {
      Console.WriteLine("Don't get yourself in trouble, okay?");
    }
    else if (user_age < 18)
    {
      Console.WriteLine("Having fun?");
    }
    Console.WriteLine("Well, i have to go now, bye!");
    Thread.Sleep(3);
    Console.Clear();
  }
}
