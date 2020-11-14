// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-scope/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Linq;

class Difference {
	private int[] elements;
	public int maximumDifference;

	// Add your code here
	public Difference(int[] elements) {
		this.elements = elements;
	}

	public int computeDifference() {
		int maxElement = elements[0];
		int minElement = elements[0];

		for (int i = 0; i < elements.Length; i++) {
			if (elements[i] < minElement) {
				minElement = elements[i];

			}
			if (elements[i] > maxElement) {
				maxElement = elements[i];
			}
		}
		maximumDifference = Math.Abs(maxElement - minElement);
		return maximumDifference;
	}
}

class Solution {
	static void Main(string[] args) {
		Convert.ToInt32(Console.ReadLine());

		int[] a = Console.ReadLine().Split(' ').Select(x = >Convert.ToInt32(x)).ToArray();

		Difference d = new Difference(a);

		d.computeDifference();

		Console.Write(d.maximumDifference);
	}
}
