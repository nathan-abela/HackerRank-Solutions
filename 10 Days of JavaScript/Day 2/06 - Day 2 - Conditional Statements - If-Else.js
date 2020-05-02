// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-if-else/problem
// Difficulty: Easy
// Max Score: 10
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function getGrade(score) {
    let grade;

    // Write your code here
    if (score > 25 && score <= 30) {
        grade = 'A';
    }
    else if (score > 20 && score <= 25) {
        grade = 'B';
    }
    else if (score > 15 && score <= 20) {
        grade = 'C';
    }
    else if (score > 10 && score <= 15) {
        grade = 'D';
    }
    else if (score > 5 && score <= 10) {
        grade = 'E';
    }
    else if (score >= 0 && score <= 5) {
        grade = 'F';
    }
    return grade;
}

function main() {
    const score = +(readLine());
    
    console.log(getGrade(score));
}
