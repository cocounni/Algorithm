const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const K = Number(input[1]);
let sensors = input[2].split(' ').map(Number);

if (K >= N) {
  console.log(0);
} else {
  sensors.sort((a, b) => a - b);
  
  const distances = [];
  for (let i = 0; i < N - 1; i++) {
    distances.push(sensors[i + 1] - sensors[i]);
  }

  distances.sort((a, b) => b - a);
  
  let totalDistance = 0;
  for (let i = K - 1; i < distances.length; i++) {
    totalDistance += distances[i];
  }

  console.log(totalDistance);
}
