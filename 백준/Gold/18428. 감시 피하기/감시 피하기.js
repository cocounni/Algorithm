const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const map = input.slice(1).map(line => line.split(" "));
const teachers = [];
const emptySpaces = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (map[i][j] === 'T') teachers.push([i, j]);
    if (map[i][j] === 'X') emptySpaces.push([i, j]);
  }
}

const directions = [
  [-1, 0], [1, 0], [0, -1], [0, 1]
];

function canAvoidSurveillance() {
  for (const [x, y] of teachers) {
    for (const [dx, dy] of directions) {
      let nx = x;
      let ny = y;
      while (nx >= 0 && ny >= 0 && nx < N && ny < N) {
        if (map[nx][ny] === 'O') break;
        if (map[nx][ny] === 'S') return false;
        nx += dx;
        ny += dy;
      }
    }
  }
  return true;
}

let foundSolution = false;

function placeWalls(count) {
  if (count === 3) {
    if (canAvoidSurveillance()) foundSolution = true;
    return;
  }

  for (let i = 0; i < emptySpaces.length; i++) {
    const [x, y] = emptySpaces[i];
    if (map[x][y] === 'X') {
      map[x][y] = 'O';
      placeWalls(count + 1);
      map[x][y] = 'X';
    }
    if (foundSolution) return;
  }
}

placeWalls(0);
console.log(foundSolution ? "YES" : "NO");
