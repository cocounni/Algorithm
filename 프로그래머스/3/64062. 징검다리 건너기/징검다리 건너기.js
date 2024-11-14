function canCross(stones, k, people) {
  let count = 0;
  
  for (let stone of stones) {
    if (stone < people) {
      count++;
      if (count >= k) return false;
    } else {
      count = 0;
    }
  }
  return true;
}

function solution(stones, k) {
  let left = 1;
  let right = 200000000;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (canCross(stones, k, mid)) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return right;
}
