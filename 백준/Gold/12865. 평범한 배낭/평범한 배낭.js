const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const stuff = [[0, 0]];

for (let i = 1; i <= N; i++) {
    const [weight, value] = input[i].split(' ').map(Number);
    stuff.push([weight, value]);
}

const knapsack = Array.from(Array(N + 1), () => Array(K + 1).fill(0));

for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= K; j++) {
        const weight = stuff[i][0];
        const value = stuff[i][1];

        if (j < weight) {
            knapsack[i][j] = knapsack[i - 1][j];
        } else {
            knapsack[i][j] = Math.max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j]);
        }
    }
}

console.log(knapsack[N][K]);
