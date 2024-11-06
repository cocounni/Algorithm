function solution(operations) {
    var answer = [];
    
    for (i=0; i<operations.length; i++) {
        let word = operations[i].split(" ")
        let command = word[0]
        let num = Number(word[1])
        
        let max = Math.max(...answer);
        let maxIndex = answer.indexOf(max);
        let min = Math.min(...answer);
        let minIndex = answer.indexOf(min); 
        
        if (command == "I") {
            answer.push(num)
        }
        else if (command == "D") {
            console.log(num)
            if (num == 1 && maxIndex !== -1) {
                answer.splice(maxIndex, 1);
            } else if (num == -1 && minIndex !== -1)  {
                answer.splice(minIndex, 1);
            }
        }
    }
    if (answer.length == 0) {
        return [0,0]
    } else {
        return [Math.max(...answer), Math.min(...answer)];
    }
}