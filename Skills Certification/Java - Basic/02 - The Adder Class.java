// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/java_basic
// Difficulty: Basic
// Language: Java 7

// ========================
//         Question
// ========================

// There are different kinds of calculators which are available in the market for different purposes. Sam wants to make a calculator which can return the sum of two integers.

// Implement the Adder class which should follow the following:

// - It should inherit from the Calculator class.
// - It should implement the method add(int a, int b) which should calculate and return the sum of two integer parameters, a and b.

// The locked stub code in the editor consists of the following:
// - An abstract class named Calculator which contains an abstract method, add(int a, int b).
// - A solution class which creates an object of the Adder class, and reads the inputs and passes them in a method called by the object of the Adder class.

// ========================
//         Solution
// ========================

import java.util.Scanner;

abstract class Calculator {
    abstract int add(int a, int b);
}

class Adder extends Calculator {
    int add(int a, int b) {
        return a + b;
    }
}

// Below is given
class Solution {
    public static void main(String[] args) {
        int a, b;
        try (Scanner scan = new Scanner(System.in)) {
            a = scan.nextInt();
            b = scan.nextInt();
        }

        Calculator adderObject = new Adder();
        System.out.println("The sum is: " + adderObject.add(a, b));
    }
}
