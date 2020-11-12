// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/java_basic
// Difficulty: Basic
// Language: Java 7

// ========================
//         Question
// ========================

// Given the following code, which are true?

interface Syrupable {
    void getSugary();
}

abstract class Pancake implements Syrupable {
}

class BlueBerryPancake implements Pancake {
    public void getSugary() {
        ;
    }
}

class SourdoughBlueBerryPancake extends BlueBerryPancake {
    void getSugary(int s) {
        ;
    }
}

// ========================
//         Solution
// ========================

// Answer: Compilation fails due to an error on line 20.
