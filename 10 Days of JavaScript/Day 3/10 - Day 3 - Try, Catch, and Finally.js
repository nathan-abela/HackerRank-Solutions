// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Complete the reverseString function
// Use console.log() to print to stdout.

function reverseString(s) {
    try {
        s = s.split("").reverse().join("");
    }
    catch (error) {
        console.log("s.split is not a function");
    }
    finally {
        console.log(s);
    }
}

function main() {
    const s = eval(readLine());
    
    reverseString(s);
}
