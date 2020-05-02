// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-binary-calculator/problem
// Difficulty: Medium
// Max Score: 30
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================
var screen = "";

function operatorFunx() {
    if (screen.indexOf("+") != -1) {
        var numbers = screen.split("+");
        var x = parseInt(numbers[0], 2);
        var y = parseInt(numbers[1], 2);
        var sum = x + y;
        var ans = sum.toString(2);
    } else if (screen.indexOf("-") != -1) {
        var numbers = screen.split("-");
        var x = parseInt(numbers[0], 2);
        var y = parseInt(numbers[1], 2);
        var sub = x - y;
        var ans = sub.toString(2);
    } else if (screen.indexOf("*") != -1) {
        var numbers = screen.split("*");
        var x = parseInt(numbers[0], 2);
        var y = parseInt(numbers[1], 2);
        var mul = x * y;
        var ans = mul.toString(2);
    } else if (screen.indexOf("/") != -1) {
		var numbers = screen.split("/");
        var x = parseInt(numbers[0], 2);
        var y = parseInt(numbers[1], 2);
        var div = x / y;
        var ans = div.toString(2);
    }
    screen = ans;
    document.getElementById("res").innerHTML = screen;
}

function key(c) {
    //console.log(screen);

    screen += c;
    document.getElementById("res").innerHTML = screen;
}

function cl() {
    screen = "";
    document.getElementById("res").innerHTML = screen;
};
