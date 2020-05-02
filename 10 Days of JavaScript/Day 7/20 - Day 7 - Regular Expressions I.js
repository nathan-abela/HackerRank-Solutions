// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-regexp-1/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function regexVar() {
    // Declare a RegExp object variable named 're'
    // It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
    var re = RegExp(/^([aeiou]).*\1$/);

    // Do not remove the return statement
    return re;
}

function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(re.test(s));
}

// ========================
//       Explanation
// ========================

/*
- ^ => matches only at the start (0th index):
- () => stores matching value captured within
- [aeiou] => matches any of the characters in the brackets
- . => matches any character:
- + => for 1 or more occurrances (this ensures str length > 3)
- \1 => matches to previously stored match.
- $ ensures that matched item is at end of the sequence
*/
