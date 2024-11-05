const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(input[0]);
if (n === 1) {
  console.log(0);
  return;
}

const tree = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [u, v, w] = input[i].split(" ").map(Number);
  tree[u].push([v, w]);
  tree[v].push([u, w]);
}

function dfs(start) {
  const distance = Array(n + 1).fill(-1);
  const stack = [[start, 0]];
  distance[start] = 0;
  
  let maxDistance = 0;
  let farthestNode = start;

  while (stack.length) {
    const [node, dist] = stack.pop();

    for (const [nextNode, weight] of tree[node]) {
      if (distance[nextNode] === -1) {
        distance[nextNode] = dist + weight;
        stack.push([nextNode, distance[nextNode]]);
        
        if (distance[nextNode] > maxDistance) {
          maxDistance = distance[nextNode];
          farthestNode = nextNode;
        }
      }
    }
  }
  
  return { farthestNode, maxDistance };
}

const firstDfs = dfs(1);
const secondDfs = dfs(firstDfs.farthestNode);

console.log(secondDfs.maxDistance);
