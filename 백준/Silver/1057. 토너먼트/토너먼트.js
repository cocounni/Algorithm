const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const n = parseInt(input[0]);
let kim = parseInt(input[1]);
let lim = parseInt(input[2]);

function tournamentRound(n, kim, lim) {
    let round = 1;

    while (kim !== lim) {
        kim = Math.ceil(kim / 2);
        lim = Math.ceil(lim / 2);
        round++;
    }

    return round - 1;
}

console.log(tournamentRound(n, kim, lim));
