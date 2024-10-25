function solution(storey) {
    let moves = 0;

    while (storey > 0) {
        const remainder = storey % 10;
        
        if (remainder > 5 || (remainder === 5 && (Math.floor(storey / 10) % 10) >= 5)) {
            moves += 10 - remainder;
            storey += 10 - remainder;
        } else {
            moves += remainder;
        }
        
        storey = Math.floor(storey / 10);
    }
    
    return moves;
}
