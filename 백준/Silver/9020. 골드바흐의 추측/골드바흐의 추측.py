# 소수 구하기 - 에레토스테네스의 체
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

t = int(input()) # test case

for _ in range(t): 
    n = int(input())
    tmp = n // 2
    
    while tmp > 0:
        if isPrime(tmp):
            if isPrime(n - tmp):
                print(tmp, n-tmp)
                break
        tmp -= 1