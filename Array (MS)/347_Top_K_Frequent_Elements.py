class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        record = {}

        for num in nums:
            if num in record:
                record[num] = record[num] + 1
            else:
                record[num] = 1

        sorted_record = sorted(record.items(), key=lambda x:x[1])
        print(sorted_record)
        result = []

        for _ in range(k):
            result.append(sorted_record.pop()[0])

        return sorted(result)



if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 2, 2, 2, 2, 3], 2))

