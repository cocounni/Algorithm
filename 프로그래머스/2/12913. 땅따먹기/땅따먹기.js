function solution(land) {
    var answer = 0;
    
    let prev = [...land[0]];
    
    for (let i=1; i<land.length; i++) {
        let current = new Array(4).fill(0);
        
        for (let j=0; j<4; j++) {
            current[j] = land[i][j] + Math.max(...prev.filter((_, idx) => idx != j));
        }
        prev = current;
    }
    
    answer = Math.max(...prev);
    
    return answer;
}