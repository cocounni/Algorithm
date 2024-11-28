function solution(places) {
    const directions = [
        [0, 1], [1, 0], [0, -1], [-1, 0]
    ];
    
    function isSafe(place, x, y) {
        const queue = [[x, y, 0]];
        const visited = Array.from({ length: 5 }, () => Array(5).fill(false));
        visited[x][y] = true;

        while (queue.length > 0) {
            const [cx, cy, distance] = queue.shift();

            for (const [dx, dy] of directions) {
                const nx = cx + dx;
                const ny = cy + dy;

                if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5 || visited[nx][ny]) {
                    continue;
                }

                visited[nx][ny] = true;

                if (place[nx][ny] === 'P' && distance < 2) {
                    return false;
                }

                if (place[nx][ny] === 'O') {
                    queue.push([nx, ny, distance + 1]);
                }
            }
        }

        return true;
    }

    function checkPlace(place) {
        for (let i = 0; i < 5; i++) {
            for (let j = 0; j < 5; j++) {
                if (place[i][j] === 'P') {
                    if (!isSafe(place, i, j)) {
                        return 0;
                    }
                }
            }
        }
        return 1;
    }

    return places.map(checkPlace);
}
