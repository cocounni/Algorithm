n = int(input())
m = int(input())
materials = list(map(int, input().split()))

materials.sort()

left = 0
right = n - 1
count = 0

while left < right:
    sum_value = materials[left] + materials[right]
    
    if sum_value == m:
        count += 1
        left += 1
        right -= 1
    elif sum_value < m:
        left += 1
    else:
        right -= 1

print(count)