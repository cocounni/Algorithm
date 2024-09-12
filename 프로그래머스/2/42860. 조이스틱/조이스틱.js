function solution(name) {
    var answer = 0;
    var nameArray = name.split('');
    var move = name.length -1;
    
    for (i = 0; i < name.length; i++) {
        answer += Math.min(name.charCodeAt(i) - 65, 91 - name.charCodeAt(i));
        
        var next = i + 1;
        while (next < name.length && name[next] === "A") {
            next ++;
        }
        
        // 1. 오른쪽으로만 가는 경우 2. 오른쪽으로 가다가 왼쪽으로 돌아가는 경우, 왼쪽으로 가다가 오른쪽으로 돌아가는 경우 세 가지 중 최소값
        move = Math.min(move, i * 2 + name.length - next, i + (name.length - next) * 2);
    }
    
    return answer + move;
    
}