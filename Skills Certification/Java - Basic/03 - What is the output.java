// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/java_basic
// Difficulty: Basic
// Language: Java 7

// ========================
//         Question
// ========================

// What is the output of the following Java Code?

interface BaseI {
   void method();
}

class BaseC {
   public void method() {
      System.out.println("Inside BaseC::method");
   }
}

class ImplC extends BaseC implements BaseI {
   public static void main(String[] s) {
      (new ImplC()).method();
   }
}

// ========================
//         Solution
// ========================

// Answer: Inside BaseC::method
