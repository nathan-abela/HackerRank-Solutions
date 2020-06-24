// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/java_basic
// Difficulty: Basic
// Language: Java 7

// ========================
//         Question
// ========================

// Write a Comparator class with the following 3 overloaded compare methods:

// - boolean compare(int a, int b): Return true if int a = int b, otherwise return false.
// - boolean compare(string a, string b): Return true if string a = string b, otherwise return false.
// - boolean compare(int[] a, int[] b): Return true if both of the following conditions hold true:
// - Arrays a and b are of equal length.
// - For each index i (where 0 ≤ i < |a|, |b|), a[i] = b[i]. Otherwise return false
// - Note: For C++, both parameters are of type Vector<int>.

// ========================
//         Solution
// ========================

import java.util.*;

class Comparator {
    boolean compare(int a, int b) {
        if (a == b) {
            return true;
        }
        return false;
    }

    boolean compare(String a, String b) {
        if (a.equals(b)) {
            return true;
        }
        return false;
    }

    boolean compare(int[] a, int[] b) {
        if (a.length != b.length) {
            return false;
        }

        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }
}

// Below is given
class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Comparator comp = new Comparator();

        int testCases = Integer.parseInt(scan.nextLine());
        while (testCases-- > 0) {
            int condition = Integer.parseInt(scan.nextLine());
            switch (condition) {
                case 1:
                    String s1 = scan.nextLine().trim();
                    String s2 = scan.nextLine().trim();

                    System.out.println((comp.compare(s1, s2)) ? "Same" : "Different");
                    break;
                case 2:
                    int num1 = scan.nextInt();
                    int num2 = scan.nextInt();

                    System.out.println((comp.compare(num1, num2)) ? "Same" : "Different");
                    if (scan.hasNext()) { // avoid exception if this last test case
                        scan.nextLine(); // eat space until next line
                    }
                    break;
                case 3:
                    // create and fill arrays
                    int[] array1 = new int[scan.nextInt()];
                    int[] array2 = new int[scan.nextInt()];
                    for (int i = 0; i < array1.length; i++) {
                        array1[i] = scan.nextInt();
                    }
                    for (int i = 0; i < array2.length; i++) {
                        array2[i] = scan.nextInt();
                    }

                    System.out.println(comp.compare(array1, array2) ? "Same" : "Different");
                    if (scan.hasNext()) { // avoid exception if this last test case
                        scan.nextLine(); // eat space until next line
                    }
                    break;
                default:
                    System.err.println("Invalid input.");
            }// end switch
        } // end while
        scan.close();
    }
}
