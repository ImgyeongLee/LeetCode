// Time complexity: O(n)
// Space complexity: O(n)
// Source
// https://leetcode.com/problems/contains-duplicate/solutions/2459020/very-easy-100-fully-explained-c-java-python-javascript-python3-creating-set/

var containsDuplicate = function (nums) {
  const s = new Set(nums);
  return s.size !== nums.length;
};
