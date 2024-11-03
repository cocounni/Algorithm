function solution(n, m, section) {
    let answer = 0;
    let currentPosition = 0;

    for (let i = 0; i < section.length; i++) {
        if (section[i] > currentPosition) {
            answer++;
            currentPosition = section[i] + m - 1;
        }
    }

    return answer;
}
