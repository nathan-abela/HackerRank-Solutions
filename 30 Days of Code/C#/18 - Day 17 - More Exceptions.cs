// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-more-exceptions/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Calculator {
	public int power(int n, int p) {
		if (n < 0 || p < 0) {
			throw new Exception("n and p should be non-negative");
		}
		else {
			return Convert.ToInt32(Math.Pow(n, p));
		}
	}
}

class Solution {
	static void Main(String[] args) {
		Calculator myCalculator = new Calculator();
		int T = Int32.Parse(Console.ReadLine());
		while (T-->0) {
			string[] num = Console.ReadLine().Split();
			int n = int.Parse(num[0]);
			int p = int.Parse(num[1]);
			try {
				int ans = myCalculator.power(n, p);
				Console.WriteLine(ans);
			}
			catch(Exception e) {
				Console.WriteLine(e.Message);
			}
		}
	}
}
