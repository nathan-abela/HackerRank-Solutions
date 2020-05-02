// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-arrows/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Modify and return the array so that all even elements are doubled and all odd elements are tripled.
// Parameter(s):
// nums: An array of numbers.

function modifyArray(nums) {
    const func = nums.map(function(num) {

    if (num % 2 == 0) {
        return 2 * num;
    }
    else {
        return 3 * num;
    }
    });
    return func;
}

function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}
