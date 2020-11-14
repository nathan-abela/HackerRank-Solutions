// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
// Difficulty: Easy
// Max Score: 30
// Language: C#

// ========================
//         Solution
// ========================

using System;

class Solution {

    static void Main(string[] args) {
        int[][] arr = new int[6][];

        for (int i = 0; i < 6; i++) {
            arr[i] = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
        }
        int result = -9 * 7;
        int rowCount = arr.Length;
        int columnCount = arr[0].Length;

        for (int c = 0; c < columnCount - 2; c++) {
            for (int r = 0; r < rowCount - 2; r++) {
                int firstRowSum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2];
                int secondRowSum = arr[r + 1][c + 1];
                int thirdRowSum = arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2];
                int totalHourGlass = firstRowSum + secondRowSum + thirdRowSum;

                result = Math.Max(result, totalHourGlass);
            }
        }

        Console.WriteLine(result);
    }
}
