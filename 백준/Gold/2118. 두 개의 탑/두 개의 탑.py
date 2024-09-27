import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
distances = list(map(int, data[1:]))

left = 0
right = 0
current_distance = distances[0]
total_distance = sum(distances)
max_distance = 0

while left < n and right < 2 * n - 1:
    max_distance = max(max_distance, min(current_distance, total_distance - current_distance))
    
    right += 1
    if right < 2 * n - 1:
        current_distance += distances[right % n]
    
    while current_distance > total_distance / 2 and left < right:
        current_distance -= distances[left % n]
        left += 1

print(max_distance)