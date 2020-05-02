// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-inheritance/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}

// Write code that adds an 'area' method to the Rectangle class' prototype
Rectangle.prototype.area = function () {
    return this.w * this.h;
}

// Create a Square class that inherits from Rectangle and implement its class constructor
class Square extends Rectangle{
    constructor(s) {
        super(s, s);
    }
}

if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);
    
    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}
