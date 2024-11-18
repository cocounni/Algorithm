function solution(N, road, K) {
    const graph = Array.from({ length: N + 1 }, () => []);
    const distances = Array(N + 1).fill(Infinity);
    const pq = [];
    
    road.forEach(([a, b, c]) => {
        graph[a].push([b, c]);
        graph[b].push([a, c]);
    });
    
    distances[1] = 0;
    pq.push([1, 0]);
    
    while (pq.length > 0) {
        const [current, currentDist] = pq.shift();
        
        if (currentDist > distances[current]) continue;
        
        for (const [next, weight] of graph[current]) {
            const distance = currentDist + weight;
            
            if (distance < distances[next]) {
                distances[next] = distance;
                pq.push([next, distance]);
            }
        }
    }
    
    return distances.filter((dist) => dist <= K).length;
}
