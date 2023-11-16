class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1

if __name__ == "__main__":
    solution = Solution()
    arr = [1,0,2,3]
    solution.duplicateZeros(arr)
    print(arr)
