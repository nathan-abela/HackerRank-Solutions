// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem
// Difficulty: Easy
// Max Score: 10
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Calculate the area of a rectangle.
// length: The length of the rectangle.
// Width: The width of the rectangle.
// Return a number denoting the rectangle's area.

function getArea(length, width) {
    return length*width;
}

// Calculate the perimeter of a rectangle.
// length: The length of the rectangle.
// Width: The width of the rectangle.
// Return a number denoting the perimeter of a rectangle.

function getPerimeter(length, width) {
    // Write your code here
    return 2*(length+width);
}

function main() {
    const length = +(readLine());
    const width = +(readLine());
    
    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}
