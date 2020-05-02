// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-throw/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Complete the isPositive function.
// If 'a' is positive, return "YES".
// If 'a' is 0, throw an Error with the message "Zero Error"
// If 'a' is negative, throw an Error with the message "Negative Error"

function isPositive(a) {
    if (a > 0) {
        return "YES";
    } 
    else if (a == 0) {
        return "Zero Error";
    } 
    else if (a < 0) {
        return "Negative Error";
    }
}

function main() {
    const n = +(readLine());
    
    for (let i = 0; i < n; i++) {
        const a = +(readLine());
      
        try {
            console.log(isPositive(a));
        } catch (e) {
            console.log(e.message);
        }
    }
}
