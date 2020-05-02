// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-class/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Implement a Polygon class with the following properties:
// 1. A constructor that takes an array of integer side lengths.
// 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.

class Polygon {
    constructor(sides) {
        this.perimeter = function() {
            var sum = 0;
            sides.forEach((value) => {
                sum += value;
            });
            return sum;
        }
    }
}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
