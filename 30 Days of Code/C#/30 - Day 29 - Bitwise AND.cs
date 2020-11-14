// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-bitwise-and/problem
// Difficulty: Medium
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
    static void Main(String[] args) {
        int t = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < t; i++) {
            string[] tokens_n = Console.ReadLine().Split(' ');
            int n = Convert.ToInt32(tokens_n[0]);
            int k = Convert.ToInt32(tokens_n[1]);

            if (((k - 1) | k) > n && k % 2 == 0) {
                Console.WriteLine(k - 2);
            }
            else {
                Console.WriteLine(k - 1);
            }
        }
    }
}
