// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-let-and-const/problem
// Difficulty: Easy
// Max Score: 10
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const r = readLine()
    const PI = Math.PI

    // Print the area of the circle:
    console.log(PI*r*r)

    // Print the perimeter of the circle:
    console.log(2*PI*r)

    try {    
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
