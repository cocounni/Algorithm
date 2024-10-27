function solution(k, ranges) {
    const hailstone = [k];
    while (k !== 1) {
        k = k % 2 === 0 ? k / 2 : k * 3 + 1;
        hailstone.push(k);
    }

    const areas = [];
    for (let i = 1; i < hailstone.length; i++) {
        const left = hailstone[i - 1];
        const right = hailstone[i];
        areas.push((left + right) / 2);
    }

    const results = [];
    const n = areas.length;
    ranges.forEach(([start, end]) => {
        end = n + end;
        if (start > end) {
            results.push(-1);
        } else {
            const rangeArea = areas.slice(start, end).reduce((sum, area) => sum + area, 0);
            results.push(rangeArea);
        }
    });

    return results;
}
