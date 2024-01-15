const fs = require('fs');

const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = inputData[0]
const B = inputData[1]

const a = B.split('')[0]
const b = B.split('')[1]
const c = B.split('')[2]

console.log(A*c)
console.log(A*b)
console.log(A*a)
console.log(A*B)