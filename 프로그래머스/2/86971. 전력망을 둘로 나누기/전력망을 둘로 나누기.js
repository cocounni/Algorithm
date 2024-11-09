function solution(n, wires) {
    const graph = Array.from({ length: n + 1 }, () => []);

    wires.forEach(([v1, v2]) => {
        graph[v1].push(v2);
        graph[v2].push(v1);
    });

    function countNodes(start, visited) {
        let count = 0;
        const queue = [start];
        visited[start] = true;

        while (queue.length > 0) {
            const node = queue.shift();
            count++;

            for (const next of graph[node]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.push(next);
                }
            }
        }

        return count;
    }

    let minDifference = n;

    wires.forEach(([v1, v2]) => {
        const visited = Array(n + 1).fill(false);
        
        graph[v1] = graph[v1].filter(node => node !== v2);
        graph[v2] = graph[v2].filter(node => node !== v1);

        const nodeCount1 = countNodes(v1, visited);
        const nodeCount2 = n - nodeCount1;
        const difference = Math.abs(nodeCount1 - nodeCount2);

        minDifference = Math.min(minDifference, difference);

        graph[v1].push(v2);
        graph[v2].push(v1);
    });

    return minDifference;
}
