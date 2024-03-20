from sys import byteorder
# H-index
def solution1(citations):
    if sum(citations) == 0:
        return 0

    maxCite = len(citations)
    record = []

    count = 1
    while count <= maxCite:
        upperBound = len([j for j in citations if j >= count])
        lowerBound = len([j for j in citations if j <= count])
        if upperBound >= count and lowerBound <= count:
            record.append(count)
        count += 1
    return max(record)

# 행렬의 곱셈
def solution2(arr1, arr2):
    cols = list(zip(*arr2))
    answer = []
    for row in arr1:
        line = []
        for col_idx in range(0, len(cols)):
            value = 0
            for i in range(0, len(cols[col_idx])):
                value += row[i] * cols[col_idx][i]
            line.append(value)
        answer.append(line)
    return answer

# 의상
def solution3(clothes):
    NAME = 0
    KIND = 1
    closet = {}

    for cloth in clothes:
        if cloth[KIND] in closet.keys():
            closet[cloth[KIND]].append(cloth[NAME])
        else:
            closet[cloth[KIND]] = [cloth[NAME]]

    combination = 1
    for key in closet.keys():
        combination *= len(closet[key]) + 1
    return combination - 1

# 튜플
def solution4(s):
    my_dict = {}
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num.isdigit():
                if int(num) in my_dict.keys():
                    my_dict[int(num)] += 1
                else:
                    my_dict[int(num)] = 1
            num = ""
    # sort by frequency in descending order
    sorted_result = list(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    answer = []
    for item in sorted_result:
        answer.append(item[0])
    return answer

if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    # print(solution4(s))
    print(byteorder)