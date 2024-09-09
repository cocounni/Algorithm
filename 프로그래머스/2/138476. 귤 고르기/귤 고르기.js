function solution(k, tangerine) {
  const countMap = new Map();

  // 귤 사이즈별로 개수 카운트
  for (let size of tangerine) {
    countMap.set(size, (countMap.get(size) || 0) + 1);
  }

  // 귤 개수 내림차순 정렬
  const sortedCounts = [...countMap.values()].sort((a, b) => b - a);

  let total = 0;  // 선택한 귤 개수
  let types = 0;  // 선택한 귤 종류의 수

  // 개수가 많은 것부터 선택
  for (let count of sortedCounts) {
    total += count;
    types++;
    if (total >= k) break;
  }

  return types;
}