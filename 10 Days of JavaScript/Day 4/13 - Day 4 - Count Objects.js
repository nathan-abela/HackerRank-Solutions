// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-count-objects/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Return a count of the total number of objects 'o' satisfying o.x == o.y.
// Parameter(s):
// objects: an array of objects with integer properties 'x' and 'y'

function getCount(objects) {
    var count = 0;

    for (let i = 0; i < objects.length; i++) {
        if (objects[i].x == objects[i].y) {
            count++;
        }
    }
    return count;    
}

function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}
