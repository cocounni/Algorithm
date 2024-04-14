#from sys import stdin as s

#s = open("input.txt", "rt")
import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    # 괄호 문자열을 한줄 씩 입력받는데, stack에 ()가 완성될 때마다 pop하고 최종적으로 아무것도 없으면 YES, 그렇지 않으면 NO를 stack에 넣기
    # arr = 괄호 문자열 한 줄 / 괄호 한 줄도 한 글자씩 끊어서 입력받기 -> list활용
    arr = list(sys.stdin.readline().strip())

    # 테스트 케이스마다 스택 초기화
    stack = []

    for alphabet in arr:
        if alphabet == "(":
            stack.append(alphabet)
        elif alphabet == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                # 닫는 괄호가 나왔으나 스택이 비어있거나 스택의 마지막 요소가 여는 괄호가 아닐 경우
                stack.append(alphabet)
                break

    # 스택이 비어있을 경우
    if not stack:
        print("YES")
    else:
        print("NO")