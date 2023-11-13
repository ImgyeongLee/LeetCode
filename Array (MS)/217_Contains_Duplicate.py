class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False
