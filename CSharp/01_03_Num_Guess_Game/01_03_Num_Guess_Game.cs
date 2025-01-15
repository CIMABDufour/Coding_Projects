// Beginner Project
// Guess number game
// The user guess a number between a range define by the user

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace CS_Code_Projects
{
    internal class Num_Guess_Game
    {
        private readonly Random random = new Random();

        private const string PlayAgainPrompt = "Do you want to play again? (yes to continue, any other key to exit): ";
        private const string ExitMessage = "The player exited the guessing game.";
        private int GetValidInteger(string prompt)
        {
            while (true)
            {
                Console.WriteLine(prompt);
                string userInput = Console.ReadLine();
                if (int.TryParse(userInput, out int number))
                {
                    return number;
                }
                else
                {
                    Console.WriteLine("Please enter a valid integer.");
                }
            }
        }

        private void New_Game()
        {
            while(true)
            {
                try
                {
                    Console.WriteLine("Welcome to the number guessing game!");

                    int range = GetValidInteger("Please enter a positive integer for the range : ");
                    int userGuess = GetValidInteger("Please enter a positive integer for the answer : ");

                    int computerNumber = random.Next(1, range-1);

                    if (userGuess == computerNumber)
                    {
                        Console.WriteLine($"Congratulations! You guessed correctly. Computer's number: {computerNumber}, Your guess: {userGuess}");
                    }
                    else
                    {
                        Console.WriteLine($"Sorry, you guessed wrong. Computer's number: {computerNumber}, Your guess: {userGuess}");
                    }

                    Console.WriteLine(PlayAgainPrompt);
                    string continueChoice = Console.ReadLine();
                    if (!continueChoice.Equals("yes", StringComparison.OrdinalIgnoreCase))
                    {
                        Console.WriteLine(ExitMessage);
                        break;
                    }
                }
                catch (Exception err)
                {
                    Console.WriteLine(err.Message);
                    Console.ReadLine();
                }
                
            }

        }
        static void Main(string[] args)
        {
            Num_Guess_Game new_guess_game = new Num_Guess_Game();
            new_guess_game.New_Game();
        }
    }
}
