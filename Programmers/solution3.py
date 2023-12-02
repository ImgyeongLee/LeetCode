# 가운데 글자 가져오기
def solution1(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]

# 수박수박수박수박수박수?
def solution2(n):
    val = n // 2
    remain = n % 2
    return "수박" * val + "수" * remain


# 문자열 내림차순으로 배치하기
def solution3(s):
    return "".join(sorted(s, reverse=True))


# 문자열 다루기 기본
# isdigit()....
def solution4(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    return False

# 행렬의 덧셈
def solution5(arr1, arr2):
    result = arr1
    biglen = len(arr1)
    length = len(arr1[0])
    for i in range(biglen):
        for j in range(length):
            result[i][j] += arr2[i][j]
    return result

# 행렬의 덧셈
def solution6(arr1, arr2):
    result = arr1
    biglen = len(arr1)
    length = len(arr1[0])
    for i in range(biglen):
        for j in range(length):
            result[i][j] += arr2[i][j]
    return result

# 최대공약수와 최소공배수
def solution7(n, m):
    answer = []
    return answer

# 이상한 문자 만들기
def solution8(s):
    count = 0
    word = ""
    for c in s:
        if ord(c) == 32:
            count = 0

        if ord(c) >= 65 and ord(c) <= 90:
            count += 1
        elif ord(c) >= 97 and ord(c) <= 122:
            count += 1

        if count % 2 == 1:
            word += c.upper()
        else:
            word += c.lower()
    return word

# 시저 암호
def solution9(s, n):
    password = ""
    for c in s:
        if ord(c) == 32:
            password += c
            continue
        cizer= ord(c) + n
        if ord(c) >= 97 and ord(c) <= 122 and cizer > 122:
            cizer = 96 + n
        elif ord(c) >= 65 and ord(c) <= 90 and cizer > 90:
            cizer = 64 + n

        password += chr(cizer)

    return password

if __name__ == "__main__":
    print(ord('Z'))
    print(solution9("a", 4))