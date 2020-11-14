// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-review-loop/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
	static void Main(String[] args) {
		int counter = Int32.Parse(Console.ReadLine());

		for (int i = 1; i <= counter; i++) {
			string myString = Console.ReadLine();

			for (int j = 0; j < myString.Length; j++) {
				if (j % 2 == 0) {
					Console.Write(myString[j]);
				}
			}

			Console.Write(" ");

			for (int j = 0; j < myString.Length; j++) {
				if (j % 2 == 1) {
					Console.Write(myString[j]);
				}
			}
			Console.WriteLine();
		}
	}
}
