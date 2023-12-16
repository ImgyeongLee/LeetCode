# 문자열 내 마음대로 정렬하기
def solution1(strings, n):
    return sorted(strings, key=lambda word: (word[n], word))


# 2016년
def solution2(a, b):
    days = ["FRI", "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_data = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Jan 1st is Friday

    current_month = 1
    current_date = 1

    while current_month < a:
        current_date += 7

        if current_date > month_data[current_month]:
            current_date -= month_data[current_month]
            current_month += 1

    while current_date < b:
        diff = abs(current_date - b)
        if diff > 7:
            current_date += 7
        elif diff == 7:
            return days[1]
        else:
            return days[diff + 1]

    return days[b - current_date]

# 모의고사
def solution3(answers):
    record = {"1": 0, "2": 0, "3": 0}
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_idx = 0
    second_idx = 0
    third_idx = 0

    first_max = len(first)
    second_max = len(second)
    third_max = len(third)

    for i in range(0, len(answers)):
        if answers[i] == first[first_idx]:
            record["1"] += 1
        if answers[i] == second[second_idx]:
            record["2"] += 1
        if answers[i] == third[third_idx]:
            record["3"] += 1

        first_idx += 1
        second_idx += 1
        third_idx += 1

        if first_idx >= first_max:
            first_idx = 0
        if second_idx >= second_max:
            second_idx = 0
        if third_idx >= third_max:
            third_idx = 0

    sorted_record = dict(sorted(record.items(), key=lambda x: x[1], reverse=True))
    result = []
    maxVal = 0
    for key in sorted_record:
        if len(result) == 0:
            result.append(int(key))
            maxVal += int(sorted_record[key])
        elif maxVal != sorted_record[key]:
            return result
        else:
            result.append(int(key))

    return result

# 실패율
def solution4(N, stages):
    pass


if __name__ == "__main__":
    print(solution3([1,3,2,4,2]))
