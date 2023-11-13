class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False


    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            count[ord(c) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True