function solution(n, times) {
    times.sort((a, b) => a - b);
    let left = 1;
    let right = times[times.length - 1] * n;
    let answer = right;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let people = 0;

        for (let time of times) {
            people += Math.floor(mid / time);
            if (people >= n) break;
        }

        if (people >= n) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return answer;
}
