class Solution(object):
    def isValid(self, s):
      if len(s) % 2 != 0:
        return False

      openings = "({["
      record = []
      for c in s:
        if c in openings:
          record.append(c)
        else:
          if len(record) == 0:
            return False
          checker = record.pop()
          if not ((checker == "(" and c == ")") or (checker == "{" and c == "}") or (checker == "[" and c == "]")):
            return False

      return len(record) == 0


if __name__ == "__main__":
  solution = Solution()
  print(solution.isValid("()[]{}"))
  print(solution.isValid("(]"))