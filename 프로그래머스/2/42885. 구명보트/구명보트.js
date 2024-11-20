function solution(people, limit) {
    var answer = 0;
    
    people.sort((a, b) => b - a);
    let start = 0;
    let end = people.length - 1;
    
    while (start <= end) {
        if (people[start] + people[end] <= limit) {
            end--;
        }
        start++;
        answer++;
    }
    
    return answer;
}