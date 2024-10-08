import heapq

def solution(book_time):
    def time_to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    book_time = [(time_to_minutes(start), time_to_minutes(end) + 10) for start, end in book_time]
    
    book_time.sort()

    rooms = []
    
    for start, end in book_time:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        
        heapq.heappush(rooms, end)
    
    return len(rooms)