from collections import Counter

def solution(weights):
    weight_count = Counter(weights)
    answer = 0
    
    ratios = [(1, 1), (2, 3), (3, 4), (1, 2)]
    
    for w in weight_count:
        if weight_count[w] > 1:
            answer += weight_count[w] * (weight_count[w] - 1) // 2
    
    weights = sorted(weight_count.keys())
    
    for i in range(len(weights)):
        for j in range(i + 1, len(weights)):
            w1, w2 = weights[i], weights[j]
            for r1, r2 in ratios[1:]:
                if w1 * r2 == w2 * r1:
                    answer += weight_count[w1] * weight_count[w2]
    
    return answer
