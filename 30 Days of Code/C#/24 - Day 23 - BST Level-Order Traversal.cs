// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-binary-trees/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;

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
	static void levelOrder(Node root) {
		//Write your code here
		Queue Q = new Queue();
		Q.Enqueue(root);

		while (Q.Count > 0) {
			Node curNode = (Node) Q.Peek();
			if (curNode.left != null) {
				Q.Enqueue(curNode.left);
			}
			if (curNode.right != null) {
				Q.Enqueue(curNode.right);
			}
			Console.Write(curNode.data + " ");
			Q.Dequeue();
		}
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
		levelOrder(root);
	}
}
