// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-arrays/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {
    static void Main(String[] args) {
        Console.ReadLine();

        var str = Console.ReadLine();
        var arr = str.Split(' ');

        Array.Reverse(arr);

        foreach(var num in arr) {
            Console.Write($"{num} ");
        }
    }
}
