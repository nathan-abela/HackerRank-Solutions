// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
// Difficulty: Medium
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

// Note: 1 is NOT a prime number, that is, a number divisable by another number less or equal to the square root of the first number, it is NOT prime

using System;

class Solution {
	static void Main(String[] args) {
		int numberOfInputs = Convert.ToInt32(Console.ReadLine());
		int i, j, inputNumber;
		string output;

		for (i = 1; i <= numberOfInputs; i++) {
			inputNumber = Convert.ToInt32(Console.ReadLine());

			for (j = 2; j <= inputNumber / j; j++) {
				if (inputNumber % j == 0) {
                    inputNumber = 1;
                }
			}
			output = inputNumber == 1 ? "Not prime": "Prime";
			Console.WriteLine(output);
		}
	}
}
