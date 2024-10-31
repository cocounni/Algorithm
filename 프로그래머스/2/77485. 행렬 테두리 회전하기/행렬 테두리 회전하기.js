function solution(rows, columns, queries) {
    const matrix = [...Array(rows)].map((_, i) => 
    [...Array(columns)].map((_, j) => i * columns + j + 1));
    const answer = [];

    for (let [x1, y1, x2, y2] of queries) {
        x1 -= 1;
        y1 -= 1;
        x2 -= 1;
        y2 -= 1;

        let temp = matrix[x1][y1];
        let minValue = temp;

        for (let i = x1; i < x2; i++) {
            matrix[i][y1] = matrix[i + 1][y1];
            minValue = Math.min(minValue, matrix[i][y1]);
        }

        for (let i = y1; i < y2; i++) {
            matrix[x2][i] = matrix[x2][i + 1];
            minValue = Math.min(minValue, matrix[x2][i]);
        }

        for (let i = x2; i > x1; i--) {
            matrix[i][y2] = matrix[i - 1][y2];
            minValue = Math.min(minValue, matrix[i][y2]);
        }

        for (let i = y2; i > y1; i--) {
            matrix[x1][i] = matrix[x1][i - 1];
            minValue = Math.min(minValue, matrix[x1][i]);
        }

        matrix[x1][y1 + 1] = temp;
        answer.push(minValue);
    }

    return answer;
}
