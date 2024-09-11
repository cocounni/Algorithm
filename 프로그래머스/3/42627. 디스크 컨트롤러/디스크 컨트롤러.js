function solution(jobs) {
    // 작업을 요청 시간을 기준으로 정렬
    jobs.sort((a, b) => a[0] - b[0]);
    
    const heap = [];
    let time = 0;
    let totalWaitTime = 0;
    let jobIndex = 0;
    let completedJobs = 0;

    while (completedJobs < jobs.length) {

        while (jobIndex < jobs.length && jobs[jobIndex][0] <= time) {
            heap.push(jobs[jobIndex]);
            jobIndex++;
        }

        // heap을 소요 시간이 짧은 순으로 정렬
        heap.sort((a, b) => a[1] - b[1]);

        if (heap.length > 0) {
            // 소요 시간이 가장 짧은 작업 처리
            const [startTime, duration] = heap.shift();

            time += duration;
            totalWaitTime += time - startTime;

            completedJobs++;
        } else {
            time = jobs[jobIndex][0];
        }
    }

    // 평균 대기 시간 계산
    return Math.floor(totalWaitTime / jobs.length);
}