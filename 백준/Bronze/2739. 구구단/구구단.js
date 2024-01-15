const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString();

const num = parseInt(inputData);

for (let i = 1; i<10; i++) {
    console.log(num + ' * ' + i + ' = ' + num*i);
}