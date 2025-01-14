// Beginner Project
// Simple Calculator Program
// Let the user calculate from the terminal with different operation +,-,*,/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace CS_Code_Project
{
    internal class Simple_Calculator
    {
        private int GetValidInteger(string prompt)
        {
            while (true)
            {
                Console.WriteLine(prompt);
                string input = Console.ReadLine();
                if (int.TryParse(input, out int result))
                {
                    return result;
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid integer.");
                }
            }
        }
        private string console_int_input()
        {
            while (true)
            {
                try
                {
                    int int_one = GetValidInteger("First Number? : ");
                    int int_two = GetValidInteger("Second Number? : ");
                    string console_result;

                    Console.WriteLine("Operator? (+, -, *, /): ");
                    string oper = Console.ReadLine();

                    switch (oper)
                    {
                        case "+":
                            Console.WriteLine($"{int_one} + {int_two} = {int_one + int_two}");
                            console_result = Console.ReadLine();
                            break;
                        case "-":
                            Console.WriteLine($"{int_one} - {int_two} = {int_one - int_two}");
                            console_result = Console.ReadLine();
                            break;
                        case "*":
                            Console.WriteLine($"{int_one} * {int_two} = {int_one * int_two}");
                            console_result = Console.ReadLine();
                            break;
                        case "/":
                            Console.WriteLine($"{int_one} / {int_two} = {int_one / int_two}");
                            console_result = Console.ReadLine();
                            break;

                        default:
                            Console.WriteLine("Invalid operator. Please use +, -, *, or /.");
                            break;

                    }
                    
                }
                catch (Exception err)
                {
                    Console.WriteLine(err.Message);
                    Console.ReadLine();
                    return null;
                }

                Console.WriteLine("Do you want to perform another calculation? (yes to continue, any other key to exit): ");
                string continueChoice = Console.ReadLine();
                if (!continueChoice.Equals("yes", StringComparison.OrdinalIgnoreCase))
                {
                    break;
                }

            }

            return null;
        }
        static void Main(string[] args)
        {
            Simple_Calculator new_calculator = new Simple_Calculator();
            new_calculator.console_int_input();
        }

    }
}
