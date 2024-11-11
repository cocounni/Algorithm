function solution(number, k) {
    let stack = [];
    let removeCount = 0;

    for (let i = 0; i < number.length; i++) {
        const num = number[i];

        while (stack.length > 0 && removeCount < k && stack[stack.length - 1] < num) {
            stack.pop();
            removeCount++;
        }

        stack.push(num);
    }

    stack = stack.slice(0, stack.length - (k - removeCount));

    return stack.join('');
}
