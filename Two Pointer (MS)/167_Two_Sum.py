class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            elif current == target:
                return [left + 1, right + 1]
            else:
                return []

# Runtime 93ms Beats 38.01%of users with Python
# Memory 14.12mb Beats 46.54%of users with Python

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))