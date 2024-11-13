const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, k] = input[0].split(' ').map(Number);
const durability = input[1].split(' ').map(Number);

let belt = durability.slice();
let robots = new Array(2 * n).fill(false);
let step = 0;

while (true) {
    step++;

    belt.unshift(belt.pop());
    robots.unshift(robots.pop());
    robots[n - 1] = false;

    for (let i = n - 2; i >= 0; i--) {
        if (robots[i] && !robots[i + 1] && belt[i + 1] > 0) {
            robots[i] = false;
            robots[i + 1] = true;
            belt[i + 1]--;
        }
    }
    robots[n - 1] = false;

    if (belt[0] > 0) {
        robots[0] = true;
        belt[0]--;
    }

    let zeroCount = 0;
    for (let i = 0; i < belt.length; i++) {
        if (belt[i] === 0) zeroCount++;
    }

    if (zeroCount >= k) break;
}

console.log(step);


