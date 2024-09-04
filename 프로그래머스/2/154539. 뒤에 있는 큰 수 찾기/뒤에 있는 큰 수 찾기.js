function solution(numbers) {
    var answer = new Array(numbers.length).fill(-1); // 기본 값은 -1
    var stack = [];
    
    for (let i = numbers.length - 1; i >= 0; i--) {
        var current = numbers[i];
        
        // 스택이 비어있지 않고, 현재 수보다 작거나 같은 수는 스택에서 제거
        while (stack.length > 0 && stack[stack.length - 1] <= current) {
            stack.pop();
        }
        
        // 스택의 맨 위에 있는 수가 현재 수보다 크면 그 수가 뒤에 있는 큰 수
        if (stack.length > 0) {
            answer[i] = stack[stack.length - 1];
        }
        
        // 현재 수를 스택에 추가
        stack.push(current);
    }
    
    return answer;
}