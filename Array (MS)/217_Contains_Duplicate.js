/**
 * @param {number[]} nums
 * @return {boolean}
 *
 * Given an integer array nums, return true if any value appears at least twice in the array,
 * and return false if every element is distinct.
 */
var containsDuplicate = function (nums) {
  var hashmap = new Map();
  var result = false;
  for (let i = 0; i < nums.length; i++) {
    if (hashmap.has(nums[i])) {
      result = true;
      break;
    }
    hashmap.set(nums[i], nums[i]);
  }

  return result;
};
