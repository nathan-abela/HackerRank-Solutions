// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-switch/problem
// Difficulty: Easy
// Max Score: 10
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function getLetter(s) {
    let letter;

    // Write your code here
    switch (s.charAt(0)) {
        case ( 'a' || 'e' || 'o' || 'i' || u):
            letter = 'A';
            break;
        case ('b' || 'c' || 'd' || 'f' || 'g'):
            letter = 'B';
            break;
        case ('h' || 'j' || 'k' || 'l' || 'm'):
            letter = 'C';
            break;
        case ('z' || 'n' || 'p' || 'q' || 'r' || 's' || 't' || 'v' || 'w' || 'x' || 'y' ):
            letter = 'D';
    }
    return letter;
}

function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}
