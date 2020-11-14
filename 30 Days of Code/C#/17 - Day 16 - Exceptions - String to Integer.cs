// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
	static void Main(String[] args) {
		string S = Console.ReadLine();

		try {
			Console.WriteLine(int.Parse(S));
		}
		catch(FormatException) {
			Console.WriteLine("Bad String");
		}
	}
}
