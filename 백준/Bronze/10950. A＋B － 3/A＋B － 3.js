const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const testCase = parseInt(inputData[0]);

for (let i=1; i<=testCase; i++) {
    let num = inputData[i].split(' ')
    
    console.log(parseInt(num[0]) + parseInt(num[1]));
}