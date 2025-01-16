//Beginner Project
//Get a joke from API
//Build a simple program that fetches jokes.
//Version one is using a class to structure and type safety when deserializing the JSON data
// A type Stopwatch is added also to measure the response time between the class, JsonDocument and Dynamic "Method"

using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Text.Json.Serialization;
using System.Diagnostics;

namespace CS_Code_Project
{
    internal class RequestJoke
    {
        private const string Url = "https://official-joke-api.appspot.com/jokes/random";

        // Async method to fetch the joke
        private async Task FetchAndPrintJokeAsync(HttpClient httpClient)
        {
            Stopwatch stopwatch = new Stopwatch();

            try
            {
                stopwatch.Start();
                // Make an HTTP GET request
                using (HttpResponseMessage response = await httpClient.GetAsync(Url))
                {
                    response.EnsureSuccessStatusCode();

                    // Read the response content as a string
                    string jsonResponse = await response.Content.ReadAsStringAsync();

                    // Parse the JSON response to extract setup and punchline
                    Joke joke = JsonSerializer.Deserialize<Joke>(jsonResponse);

                    stopwatch.Stop();

                    // Print the joke
                    if (joke != null)
                    {
                        Console.WriteLine($"Setup: {joke.Setup}");
                        Console.WriteLine($"Punchline: {joke.Punchline}\n");
                    }
                }

                Console.WriteLine($"Time taken for the HTTP request: {stopwatch.ElapsedMilliseconds} ms");

            }
            catch (Exception ex)
            {
                stopwatch.Stop();
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        static async Task Main(string[] args)
        {
            RequestJoke newJoke = new RequestJoke();
            HttpClient httpClient = new HttpClient();

            // Await the async method
            await newJoke.FetchAndPrintJokeAsync(httpClient);

            Console.WriteLine("Press Enter to exit.");
            Console.ReadLine();
        }
    }

    // Define a class to represent the JSON response
    public class Joke
    {
        [JsonPropertyName("type")]
        public string Type { get; set; }

        [JsonPropertyName("setup")]
        public string Setup { get; set; }

        [JsonPropertyName("punchline")]
        public string Punchline { get; set; }

        [JsonPropertyName("id")]
        public int Id { get; set; }
    }
}
