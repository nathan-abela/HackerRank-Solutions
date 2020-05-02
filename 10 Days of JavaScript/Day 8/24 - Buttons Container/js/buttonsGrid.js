// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-buttons-container/problem
// Difficulty: Easy
// Max Score: 25
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");
let btn7 = document.getElementById("btn7");
let btn8 = document.getElementById("btn8");
let btn9 = document.getElementById("btn9");

function clockwiseRotation() {
    [btn1.innerHTML,
        btn2.innerHTML,
        btn3.innerHTML,
        btn4.innerHTML,
        btn6.innerHTML,
        btn7.innerHTML,
        btn8.innerHTML,
        btn9.innerHTML
    ] = [btn4.innerHTML,
        btn1.innerHTML,
        btn2.innerHTML,
        btn7.innerHTML,
        btn3.innerHTML,
        btn8.innerHTML,
        btn9.innerHTML,
        btn6.innerHTML
    ]
}

btn5.addEventListener("click", clockwiseRotation)