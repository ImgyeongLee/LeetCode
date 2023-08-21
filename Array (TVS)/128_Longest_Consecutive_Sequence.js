var longestConsecutive = function (arr) {
  if (arr.length <= 0) return 0;

  let map = new Map();

  // Create a map
  for (let elem of arr) {
    map.set(elem, 1);
  }

  for (let i in arr) {
    if (map.has(arr[i] - 1)) {
      map.set(arr[i], 0);
    }
  }

  let maxLen = 1;
  for (let elem of arr) {
    if (map.get(elem) == 1) {
      let seqCount = 1;
      while (map.has(elem + seqCount)) {
        seqCount += 1;
      }

      maxLen = Math.max(maxLen, seqCount);
    }
  }

  return maxLen;
};

// Reference: Leetcode @KaziNizamul
