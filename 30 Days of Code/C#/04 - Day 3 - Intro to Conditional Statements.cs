// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-conditional-statements/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
    static void Main(String[] args) {
        var n = int.Parse(Console.ReadLine());

        if (n % 2 != 0) {
            Console.WriteLine("Weird");
        }
        else {
            if (n <= 5) { 
                Console.WriteLine("Not Weird");
            }
            else if (n <= 20) {
                Console.WriteLine("Weird");
            }
            else {
                Console.WriteLine("Not Weird");
            }
        }
    }
}
