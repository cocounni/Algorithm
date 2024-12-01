const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M, L] = input[0].split(' ').map(Number);
const restStops = N > 0 ? input[1].split(' ').map(Number) : [];

restStops.push(0, L);
restStops.sort((a, b) => a - b);

function canInstall(mid) {
    let count = 0;
    for (let i = 1; i < restStops.length; i++) {
        const distance = restStops[i] - restStops[i - 1];
        count += Math.floor((distance - 1) / mid);
    }
    return count <= M;
}

let left = 1;
let right = L;
let answer = 0;

while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (canInstall(mid)) {
        answer = mid;
        right = mid - 1;
    } else {
        left = mid + 1;
    }
}

console.log(answer);