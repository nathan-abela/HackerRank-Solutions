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
		int n = Int32.Parse(Console.ReadLine());
		Dictionary < string,
		string > phonebook = new Dictionary < string,
		string > ();

		for (int i = 0; i < n; i++) {
			string[] line = Console.ReadLine().Split(' ');
			phonebook[line[0]] = line[1];
		}

		string name;
		while ((name = Console.ReadLine()) != null) {
			if (phonebook.ContainsKey(name)) {
				Console.WriteLine(name + "=" + phonebook[name]);
			}
			else {
				Console.WriteLine("Not found");
			}
		}
	}
}
