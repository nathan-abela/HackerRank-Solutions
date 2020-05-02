// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-bitwise/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

function getMaxLessThanK(n, k) {
    let maximum = 0;
    let current = -1;

    for (let i = 1; i < n; i++) {
        for (let j = i + 1; j <= n; j++) {
            current = i & j;
            if (current < k && current > maximum) {
                maximum = current;
            }
        }
    }
    return maximum;
}

function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}
