// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-sorting/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
    static void Main(String[] args) {
        int numberInput = Convert.ToInt32(Console.ReadLine());

        string[] arrayInput = Console.ReadLine().Split(' ');
        int[] numbersArray = Array.ConvertAll(arrayInput, Int32.Parse);
        
        // Write Your Code Here
        int numberOfSwaps = 0;

        for (int i = 0; i < numberInput; i++) {
            for (int j = 0; j < numberInput - 1; j++) {
                if (numbersArray[j] > numbersArray[j + 1]) {
                    Array.Reverse(numbersArray, j, 2);
                    numberOfSwaps++;
                }
            }

            if (numberOfSwaps == 0) {
                break;
            }
        }

        int firstPosition = numbersArray[0];
        int lastPosition = numbersArray[numbersArray.Length - 1];

        Console.WriteLine($"Array is sorted in {numberOfSwaps} swaps.");
        Console.WriteLine($"First Element: {firstPosition}");
        Console.WriteLine($"Last Element: {lastPosition}");
    }
}
