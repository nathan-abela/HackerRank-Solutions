// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Collections.Generic;

class Solution {
	static void Main(String[] args) {
		var n = int.Parse(Console.ReadLine());

		Console.WriteLine(factorial(n));
	}

	// Complete the factorial function below.
	static int factorial(int n) {
		if (n == 1) {
			return 1;
		}

		return factorial(n - 1) * n;
	}
}
