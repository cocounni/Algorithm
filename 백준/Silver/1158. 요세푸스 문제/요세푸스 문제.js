const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const [n, k] = input.split(" ").map(Number);

const josephus = (n, k) => {
  const queue = Array.from({ length: n }, (_, i) => i + 1);
  const result = [];

  let index = 0;
  while (queue.length > 0) {
    index = (index + k - 1) % queue.length;
    result.push(queue.splice(index, 1)[0]);
  }

  return `<${result.join(", ")}>`;
};

console.log(josephus(n, k));
