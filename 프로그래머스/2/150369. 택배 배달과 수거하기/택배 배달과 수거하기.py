def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliver_count = 0
    pickup_count = 0
    
    for i in range(n - 1, -1, -1):
        deliver_count += deliveries[i]
        pickup_count += pickups[i]
        
        while deliver_count > 0 or pickup_count > 0:
            answer += (i + 1) * 2
            
            deliver_count -= cap
            pickup_count -= cap
    
    return answer