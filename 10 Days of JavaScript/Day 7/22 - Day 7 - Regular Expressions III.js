// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-regexp-3/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function regexVar() {
    // Declare a RegExp object variable named 're'
    // It must match ALL occurrences of numbers in a string.
    var re = RegExp('\\d+', 'g');

    // Do not remove the return statement
    return re;
}

function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(re.test(s));
}
