// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Collections.Generic;
using System.IO;

abstract class Book {

	protected String title;
	protected String author;

	public Book(String t, String a) {
		title = t;
		author = a;
	}
	public abstract void display();

}

//Write MyBook class
class MyBook : Book {
	private int price = 0;
	public MyBook(String title, String author, int price) : base(title, author) {
		this.price = price;
	}

	public override void display() {
		Console.Write("Title: {0} \nAuthor: {1} \nPrice: {2}", title, author, price);
	}
}

class Solution {
	static void Main(String[] args) {
		String title = Console.ReadLine();
		String author = Console.ReadLine();
		int price = Int32.Parse(Console.ReadLine());
		Book new_novel = new MyBook(title, author, price);
		new_novel.display();
	}
}
