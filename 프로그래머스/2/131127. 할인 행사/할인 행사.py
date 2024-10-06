from collections import Counter

def solution(want, number, discount):
    need = {want[i]: number[i] for i in range(len(want))}
    
    N = len(discount)
    
    answer = 0
    
    for i in range(N - 9):
        current_window = Counter(discount[i:i+10])
        
        valid = True
        for item, count in need.items():
            if current_window[item] < count:
                valid = False
                break
        
        if valid:
            answer += 1
    
    return answer