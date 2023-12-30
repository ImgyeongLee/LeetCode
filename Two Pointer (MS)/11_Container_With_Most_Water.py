class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = -1
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([]))