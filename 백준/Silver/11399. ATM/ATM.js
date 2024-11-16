const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0]);
const times = input[1].split(' ').map(Number);

times.sort((a, b) => a - b);

let total = 0;
let sum = 0;

for (let i = 0; i < n; i++) {
    sum += times[i];
    total += sum;
}

console.log(total);
