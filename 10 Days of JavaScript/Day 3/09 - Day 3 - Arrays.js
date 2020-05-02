// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-arrays/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Return the second largest number in the array.
// @param {Number[]} nums - An array of numbers.
// @return {Number} The second largest number in the array.

function getSecondLargest(nums) {
    // Complete the function
    nums.sort((a, b) => a < b); // This sorts inversely
    var a = nums.shift();

    while (a == nums[0]) {
        a = nums.shift();
    }
    a = nums.shift();

    return a;
}

function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
