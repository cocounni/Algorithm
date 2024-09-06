const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const hookedFruits = input[1].split(' ').map(Number);

function Tanghulu() {
    let l = 0, r = 0, answer = 0;

    // fruitNumCnt = 막대에 꽂힌 과일 종류 개수 카운트
    let fruitNumCnt = 0;
    let fruitsArr = Array(10).fill(0); // 10칸 카운팅 배열

    while (r < N) {
        if (fruitsArr[hookedFruits[r]] === 0) {
            fruitNumCnt++; // 새로운 과일 종류라면 카운트 증가
        }
        fruitsArr[hookedFruits[r]]++; // 현재 과일의 빈도수 증가
        r++; // 포인터 오른쪽으로 이동

        // 꽂은 과일 종류가 2종류를 넘으면 왼쪽 포인터를 이동
        while (fruitNumCnt > 2) {
            fruitsArr[hookedFruits[l]]--; // 왼쪽 포인터가 가리키는 과일의 빈도 감소
            if (fruitsArr[hookedFruits[l]] === 0) {
                fruitNumCnt--; // 과일 빈도가 0개가 되면 카운트 감소
            }
            l++; // 왼쪽 포인터 이동
        }

        // 현재 부분 배열의 길이를 갱신
        answer = Math.max(answer, r - l);
    }

    console.log(answer);
}

Tanghulu();