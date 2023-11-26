class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left = 1
        right = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = right;
            right *= nums[i];

        for i in range(len(nums)):
            result[i] *= left;
            left *= nums[i];

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))