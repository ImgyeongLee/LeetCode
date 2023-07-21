/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let map = new Map();
  nums.forEach((num) => {
    map.has(num) ? map.set(num, map.get(num) + 1) : map.set(num, 1);
  });

  const sortedMap = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));
  const iterator = sortedMap.entries();
  const result = [];

  for (let i = 0; i < k; i++) {
    result.push(iterator.next().value[0]);
  }

  return result;
};

// Runtime - 72ms   | Beats 77.22%of users with JavaScript
// Memory - 44.77mb | Beats 79.76%of users with JavaScript
