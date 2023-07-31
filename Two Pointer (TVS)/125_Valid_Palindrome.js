const isPalindrome = (s) => {
  s = s.toLowerCase().replace(/[_\W]/g, "");

  // WHATTTTTT
  for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
    if (s[i] !== s[j]) return false;
  }
  return true;
};

// Source: LeetCode - @i-love-typescript
