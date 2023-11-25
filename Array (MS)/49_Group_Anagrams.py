class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for str in strs:
            original = str
            word = "".join(sorted(str))
            if word in result:
                result[word].append(original)
            else:
                result[word] = [original]
        return result.values()


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["ab", "ba", "abc"]))
