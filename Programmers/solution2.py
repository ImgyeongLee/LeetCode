import math

# 문자열을 정수로 바꾸기
def solution1(s):
    isNegative = False
    if s[0] == '-':
        isNegative = True
        s = s[1:]

    return -int(s) if isNegative else int(s)

# 자연수 뒤집어 배열로 만들기
def solution2(n):
    answer = []
    n = str(n)
    for num in n[::-1]:
        answer.append(int(num))
    return answer

# 정수 제곱근 판별
'''
Maybe using "sqrt = n ** (1/2)" would be better.
Then, we can check the remains of sqrt. (divided by 1)
'''
def solution3(n):
    num = math.floor(math.sqrt(n))
    compare = math.floor(math.pow(num, 2))

    if n == compare:
        return math.floor(math.pow(num + 1, 2))
    return -1

# 정수 내림차순으로 배치하기
def solution4(n):
    return int("".join(sorted(str(n), reverse=True)))

# 하샤드 수
def solution5(x):
    sumNum = 0
    for c in str(x):
        sumNum += int(c)
    return True if x % sumNum == 0 else False

# 두 정수 사이의 합
'''
You can combine sum() function and for-loop.
Like this: sum(range(a, b + 1))
Also, we don't need to declare one more variable to swap two variables.
Just use a, b = b, a
'''
def solution6(a, b):
    if a == b:
        return a

    if a > b:
        temp = b
        b = a
        a = temp

    answer = 0

    for num in range(a, b + 1):
        answer += num

    return answer

# 콜라츠 추측
def recursive_helper(num, count):
    if num == 1:
        return count

    if count > 500:
        return -1

    if num % 2 == 0:
        return recursive_helper(num // 2, count + 1)
    else:
        return recursive_helper(num * 3 + 1, count + 1)


def solution7(num):
    return recursive_helper(num, 0)

# 서울에서 김서방 찾기
'''
You can use index function as well.
'''
def solution8(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"
    return None


# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    if len(answer) == 0:
        return [-1]

    return sorted(answer)

# From peer review: element > divisor (additional condition -> increase speed efficiency)


# 핸드폰 번호 가리기
def solution10(phone_number):
    n = len(phone_number) - 4

    if n == 0:
        return phone_number

    return "*" * n + phone_number[-4:]

# 제일 작은 수 제거하기
def solution11(arr):
    if len(arr) == 1:
        return [-1]

    value = min(arr)
    arr.remove(value)
    return arr

if __name__ == "__main__":
    print(solution10("465162785"))
