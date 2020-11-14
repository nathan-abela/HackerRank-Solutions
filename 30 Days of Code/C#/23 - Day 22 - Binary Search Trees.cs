// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Node {
	public Node left,
	right;
	public int data;
	public Node(int data) {
		this.data = data;
		left = right = null;
	}
}

class Solution {

	static int getHeight(Node root) {
		//Write your code here
		if (root == null) {
			return - 1;
		}

		return 1 + Math.Max(getHeight(root.left), getHeight(root.right));
	}

	static Node insert(Node root, int data) {
		if (root == null) {
			return new Node(data);
		}
		else {
			Node cur;
			if (data <= root.data) {
				cur = insert(root.left, data);
				root.left = cur;
			}
			else {
				cur = insert(root.right, data);
				root.right = cur;
			}
			return root;
		}
	}
    
	static void Main(String[] args) {
		Node root = null;
		int T = Int32.Parse(Console.ReadLine());
		while (T-->0) {
			int data = Int32.Parse(Console.ReadLine());
			root = insert(root, data);
		}
		int height = getHeight(root);
		Console.WriteLine(height);
	}
}
