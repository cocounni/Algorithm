const fs = require('fs');

const inputData = fs.readFileSync('/dev/stdin').toString()

const num = parseInt(inputData)

for (let i=1; i<=num; i++) {
    console.log('*'.repeat(i))
}