class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered_word = ''.join(c for c in s if c.isalnum()).lower()
        length = len(filtered_word)

        left = 0
        right = length - 1
        while left < right:
            if filtered_word[left] != filtered_word[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("race a car"))