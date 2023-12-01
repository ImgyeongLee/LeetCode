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


def solution5(arr1, arr2):
    pass


if __name__ == "__main__":
    print([1, 2] + [1, 4])