class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = a + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    answer.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return answer