// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-linked-list/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
class Node {
	public int data;
	public Node next;
	public Node(int d) {
		data = d;
		next = null;
	}

}
class Solution {
	public static Node insert(Node head, int data) {
		//Complete this method
		Node node = new Node(data);
		if (head == null) {
			head = node;
		}
		else {
			if (head.next == null) {
				head.next = node;
			}
			else {
				Node current = head;
				while (current.next != null) {
					current = current.next;
				}
				current.next = node;
			}
		}
		return head;
	}

	public static void display(Node head) {
		Node start = head;
		while (start != null) {
			Console.Write(start.data + " ");
			start = start.next;
		}
	}
	static void Main(String[] args) {

		Node head = null;
		int T = Int32.Parse(Console.ReadLine());
		while (T-->0) {
			int data = Int32.Parse(Console.ReadLine());
			head = insert(head, data);
		}
		display(head);
	}
}
