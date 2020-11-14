// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-inheritance/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Linq;

class Person {
	protected string firstName;
	protected string lastName;
	protected int id;

	public Person() {}
	public Person(string firstName, string lastName, int identification) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.id = identification;
	}
	public void printPerson() {
		Console.WriteLine("Name: " + lastName + ", " + firstName + "\nID: " + id);
	}
}

class Student: Person {
	private int[] testScores;

	// Class Constructor

	/* Parameters: 
    *  firstName - A string denoting the Person's first name.
    *  lastName - A string denoting the Person's last name.
    *  id - An integer denoting the Person's ID number.
    *  scores - An array of integers denoting the Person's test scores. */

	// Write your constructor here
	public Student(string firstName, string lastName, int id, int[] scores) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.id = id;
		this.testScores = scores;
	}

    // Method Name: Calculate
    // Return: A character denoting the grade.

    // Write your method here
    public string Calculate() {
        var average = testScores.Average();
        var res = IsWithin(average, 90, 100) ? "O" : 
                    IsWithin(average, 80, 89) ? "E" :
                    IsWithin(average, 70, 79) ? "A" :
                    IsWithin(average, 50, 69) ? "P" :
                    IsWithin(average, 40, 54) ? "D" :
                    "T";
        return res;

    }

    private bool IsWithin(double value, int minimum, int maximum) {
		return value >= minimum && value <= maximum;
	}
}

class Solution {
	static void Main() {
		string[] inputs = Console.ReadLine().Split();
		string firstName = inputs[0];
		string lastName = inputs[1];
		int id = Convert.ToInt32(inputs[2]);
		int numScores = Convert.ToInt32(Console.ReadLine());
		inputs = Console.ReadLine().Split();
		int[] scores = new int[numScores];
		for (int i = 0; i < numScores; i++) {
			scores[i] = Convert.ToInt32(inputs[i]);
		}

		Student s = new Student(firstName, lastName, id, scores);
		s.printPerson();
		Console.WriteLine("Grade: " + s.Calculate() + "\n");
	}
}
