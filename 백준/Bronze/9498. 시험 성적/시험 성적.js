const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString();

const data = parseInt(inputData);

if (data >= 90 && data <= 100) {
    console.log('A');
} else if (90 > data && data >= 80) {
    console.log('B');
} else if (80 > data && data >= 70) {
    console.log('C');
} else if (70 > data && data >= 60) {
    console.log('D');
} else {
    console.log('F');
}