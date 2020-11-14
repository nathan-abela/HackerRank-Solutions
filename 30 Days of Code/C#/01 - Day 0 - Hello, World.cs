// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-hello-world/problem
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
		// Declare a variable named 'inputString' to hold our input.
		String inputString;

		// Read a full line of input from stdin (cin) and save it to our variable, input_string.
		inputString = Console.ReadLine();

		// Print a string literal saying "Hello, World." to stdout using cout.
		Console.WriteLine("Hello, World.");

		// TODO: Write a line of code here that prints the contents of input_string to stdout.
		Console.WriteLine(inputString);
	}
}
