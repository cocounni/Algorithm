from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for dungeon_order in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for required, consume in dungeon_order:
            if current_fatigue >= required:
                current_fatigue -= consume
                count += 1
            else:
                break
        
        max_count = max(max_count, count)
    
    return max_count
