def electricWire(n, wires):
    wires.sort(key=lambda x: x[0])
    
    b_values = [wire[1] for wire in wires]
    
    # LIS(최장 증가 부분 수열) 구하기
    dp = []
    
    for b in b_values:
        # dp에서 b가 들어갈 위치 찾기
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < b:
                left = mid + 1
            else:
                right = mid
        # 위치가 dp의 길이와 같으면 새로운 값을 추가
        if left == len(dp):
            dp.append(b)
        # 그렇지 않으면 해당 위치 값을 갱신
        else:
            dp[left] = b

    return n - len(dp)

n = int(input())
wires = [tuple(map(int, input().split())) for _ in range(n)]
print(electricWire(n, wires))