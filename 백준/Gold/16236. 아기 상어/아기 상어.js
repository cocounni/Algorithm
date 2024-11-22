const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const board = input.slice(1).map(line => line.split(' ').map(Number));

const dx = [-1, 0, 1, 0];
const dy = [0, -1, 0, 1];

let sharkSize = 2;
let eaten = 0;
let time = 0;

let sharkX, sharkY;

for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (board[i][j] === 9) {
            sharkX = i;
            sharkY = j;
            board[i][j] = 0;
        }
    }
}

const bfs = () => {
    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    const queue = [[sharkX, sharkY, 0]];
    visited[sharkX][sharkY] = true;

    const fish = [];

    while (queue.length) {
        const [x, y, dist] = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            if (visited[nx][ny] || board[nx][ny] > sharkSize) continue;

            visited[nx][ny] = true;

            if (board[nx][ny] > 0 && board[nx][ny] < sharkSize) {
                fish.push([nx, ny, dist + 1]);
            }

            queue.push([nx, ny, dist + 1]);
        }
    }

    if (fish.length === 0) return null;

    fish.sort((a, b) => {
        if (a[2] !== b[2]) return a[2] - b[2];
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    });

    return fish[0];
};

while (true) {
    const fish = bfs();

    if (!fish) break;

    const [fx, fy, dist] = fish;
    sharkX = fx;
    sharkY = fy;
    time += dist;

    board[fx][fy] = 0;
    eaten += 1;

    if (eaten === sharkSize) {
        sharkSize += 1;
        eaten = 0;
    }
}

console.log(time);
