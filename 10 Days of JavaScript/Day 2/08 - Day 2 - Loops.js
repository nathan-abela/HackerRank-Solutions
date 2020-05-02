// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-loops/problem
// Difficulty: Easy
// Max Score: 10
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Complete the vowelsAndConsonants function.
// Print your output using 'console.log()'.

function vowelsAndConsonants(s) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    var vowels_array = [];
    var consonants = "";

    for(var idx = 0; idx<s.length; idx++) {
        if (vowels.indexOf(s[idx]) !== -1) {
            console.log(s[idx]);
        } else {
            consonants += s[idx] + '\n';
        }
    }
    console.log(consonants);
}

function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
