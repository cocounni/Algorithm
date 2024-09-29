from collections import Counter

def solution(topping):
    totalCounter = Counter(topping)
    leftSet = set()
    
    answer = 0
    
    for t in topping:
        leftSet.add(t)
        totalCounter[t] -= 1
        
        if totalCounter[t] == 0:
            del totalCounter[t]
        
        if len(leftSet) == len(totalCounter):
            answer += 1
    
    return answer