// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/30-generics/problem
// Difficulty: Easy
// Max Score: 30
// Language: Java

// ========================
//         Solution
// ========================

// This problem does not have the option to be done in Python, hence, Java 8 was chosen

import java.util.*;

class Printer <T> {
    // Write your code here
    public static <E> void printArray(E[] generic) {
        for(E element : generic) {
            System.out.println(element); 
        }
    }
}

public class Generics {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        
        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if(Printer.class.getDeclaredMethods().length > 1) {
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    } 
}
