// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-data-types/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Collections.Generic;
using System.IO;

class Solution {
	static void Main(String[] args) {
		// Pre-initialised variables
		int i = 4;
		double d = 4.0;
		string s = "HackerRank ";

		// Declare second integer, double, and String variables.
		int i2;
		double d2;
		string s2;

		// Read and save an integer, double, and String to your variables.
		i2 = int.Parse(Console.ReadLine());
		d2 = double.Parse(Console.ReadLine());
		s2 = Console.ReadLine();

		// Print the sum of both integer variables on a new line.
		Console.WriteLine(i + i2);

		// Print the sum of the double variables on a new line. With Format -> F1
		Console.WriteLine("{0:F1}", d + d2);

		// Concatenate and print the String variables on a new line
		// The 's' variable above should be printed first.
		Console.WriteLine("{0}{1}", s, s2);
	}
}
