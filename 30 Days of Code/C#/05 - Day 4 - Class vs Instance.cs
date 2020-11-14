// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-class-vs-instance/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Collections.Generic;
using System.IO;

class Person {
	public int age;

	public Person(int initialAge) {
		// Add some more code to run some checks on initialAge
		if (initialAge > 0) {
			age = initialAge;
		}
		else {
			Console.WriteLine("Age is not valid, setting age to 0.");
			age = 0;
		}
	}
	public void amIOld() {
		// Determining if this person's age is old
		if (age < 13) {
			Console.WriteLine("You are young.");
		}
		else if (age < 18) {
			Console.WriteLine("You are a teenager.");
		}
		else {
			Console.WriteLine("You are old.");
		}
	}

	public void yearPasses() {
		// Incrementing the age of the person
		age++;
	}
}

class Solution {
	public static void Main(String[] args) {
		int T = int.Parse(Console.In.ReadLine());
		for (int i = 0; i < T; i++) {
			int age = int.Parse(Console.In.ReadLine());
			Person p = new Person(age);
			p.amIOld();
			for (int j = 0; j < 3; j++) {
				p.yearPasses();
			}
			p.amIOld();
			Console.WriteLine();
		}
	}
}
