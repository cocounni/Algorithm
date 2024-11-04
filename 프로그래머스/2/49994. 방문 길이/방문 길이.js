function solution(dirs) {
    const visitedPaths = new Set();
    let x = 0, y = 0;

    const move = {
        'U': [0, 1],
        'D': [0, -1],
        'R': [1, 0],
        'L': [-1, 0]
    };

    for (let dir of dirs) {
        const [dx, dy] = move[dir];
        const nx = x + dx;
        const ny = y + dy;

        if (nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5) {
            const path1 = `${x},${y},${nx},${ny}`;
            const path2 = `${nx},${ny},${x},${y}`;
            visitedPaths.add(path1);
            visitedPaths.add(path2);

            x = nx;
            y = ny;
        }
    }

    return visitedPaths.size / 2;
}
