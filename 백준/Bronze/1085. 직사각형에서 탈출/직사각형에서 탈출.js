const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const x = parseInt(inputData[0])
const y = parseInt(inputData[1])
const w = parseInt(inputData[2])
const h = parseInt(inputData[3])

let a = w - x;
let b = h - y;

const minValue = Math.min(a, b, x, y);

console.log(minValue);