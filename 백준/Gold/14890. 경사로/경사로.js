function canPlaceSlope(line, L) {
    const n = line.length;
    const placed = Array(n).fill(false);

    for (let i = 0; i < n - 1; i++) {
        if (line[i] === line[i + 1]) continue;
        if (Math.abs(line[i] - line[i + 1]) > 1) return false;

        if (line[i] > line[i + 1]) {
            for (let j = 1; j <= L; j++) {
                if (i + j >= n || line[i + 1] !== line[i + j] || placed[i + j]) return false;
                placed[i + j] = true;
            }
        } else {
            for (let j = 0; j < L; j++) {
                if (i - j < 0 || line[i] !== line[i - j] || placed[i - j]) return false;
                placed[i - j] = true;
            }
        }
    }
    return true;
}

function countValidPaths(N, L, map) {
    let count = 0;

    for (let i = 0; i < N; i++) {
        if (canPlaceSlope(map[i], L)) count++;
    }

    for (let j = 0; j < N; j++) {
        const column = [];
        for (let i = 0; i < N; i++) {
            column.push(map[i][j]);
        }
        if (canPlaceSlope(column, L)) count++;
    }

    return count;
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, L] = input[0].split(" ").map(Number);
const map = input.slice(1).map(line => line.split(" ").map(Number));

console.log(countValidPaths(N, L, map));
