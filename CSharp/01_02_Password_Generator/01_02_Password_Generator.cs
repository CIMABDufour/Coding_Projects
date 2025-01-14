// Beginner Project
// A random password generator
// Create a random password for a user


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_Code_Project
{
    internal class Password_Generator
    {

        private const int char_minim = 8;
        private const string charSet = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*_-+";
       
        Random random = new Random();
        StringBuilder passwordBuilder = new StringBuilder();
        private int GetPasswordLength()
        {
            while (true)
            {
                Console.WriteLine("Enter the desired length of the password: ");
                string user_input = Console.ReadLine();

                if(int.TryParse(user_input, out int length) && length > char_minim)
                {
                    return length;
                }
                else
                {
                    Console.WriteLine($"Please enter a valid integer greater than or equal to {char_minim}.");
                }
            }
        }

        private string generate_password(int length)
        {
            
            try
            {
                for (int i = 0; i < length; i++)
                {
                    int index = random.Next(charSet.Length);
                    passwordBuilder.Append(charSet[index]);
                }

                return passwordBuilder.ToString();
            }
            catch(Exception err)
            {
                Console.WriteLine(err.Message);
                Console.ReadLine();
            }

            return null;
        }

        static void Main(string[] args)
        {
            Password_Generator generator = new Password_Generator();

            int passwordln = generator.GetPasswordLength();
            string new_pass = generator.generate_password(passwordln);
            Console.WriteLine($"Generated Password: {new_pass}");
            Console.WriteLine("Press Enter to exit.");
            Console.ReadLine();
        }
    }
}
