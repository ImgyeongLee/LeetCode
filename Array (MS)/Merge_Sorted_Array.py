class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        idx = m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[idx] = nums1[a]
                a -= 1
            else:
                nums1[idx] = nums2[b]
                b -= 1

            idx -= 1



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
