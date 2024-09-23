def solution(order):
    answer = 0
    stack = []  # 보조 컨테이너
    currentBox = 1

    for box in order:
        while currentBox <= box:
            stack.append(currentBox)
            currentBox += 1
        
        if stack[-1] == box:
            stack.pop()
            answer += 1
        else:
            break

    return answer