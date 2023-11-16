class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            supplement = target - nums[i]
            if supplement in record:
                return [record[supplement], i]
            else:
                record[nums[i]] = i

        return []
