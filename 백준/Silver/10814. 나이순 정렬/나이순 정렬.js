const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [3, '21 Junkyu', '21 Dohyun', '20 Sunyoung'];

input.shift();

input.sort((a,b) => parseInt(a.split(' ')[0]) - parseInt(b.split(' ')[0]));

console.log(input.join('\n'));