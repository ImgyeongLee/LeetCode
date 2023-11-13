# Date: Nov 12, 2023

# 약수의 합
def solution1(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer

# x만큼 간격이 있는 n개의 숫자
def solution2(x, n):
    result = []
    gap = x

    for _ in range(n):
        result.append(x)
        x += gap

    return result

# 짝수와 홀수
def solution3(num):
    return "Even" if num % 2 == 0 else "Odd"
