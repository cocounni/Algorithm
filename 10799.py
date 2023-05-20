# from sys import stdin as s

# s = open("input.txt", "rt")
text = list(input())

stack = []      # 현재 존재하는 쇠막대기 수
count = 0       # 잘린 막대기 수 count

for i in range(len(text)):
    if text[i] == "(":
        stack.append(i)
        
    else:      # else이므로 text[i] == ")"를 의미
        if text[i-1] == "(":        #()괄호 레이저 완성        
            stack.pop()
            count += len(stack)

        else:
            stack.pop()
            count += 1

print(count)