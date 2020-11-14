// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-loops/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
	static void Main(String[] args) {
		var n = int.Parse(Console.ReadLine());

		for (int i = 1; i < 11; i++) {
			Console.WriteLine($ "{n} x {i} = {n * i}");
		}
	}
}
