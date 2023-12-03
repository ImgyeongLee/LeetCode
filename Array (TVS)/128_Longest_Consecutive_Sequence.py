class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        count = 1
        maxValue = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    maxValue = max(count, maxValue)
                    count = 1

        return max(maxValue, count)

if __name__ == "__main__":
  solution = Solution()
  print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))