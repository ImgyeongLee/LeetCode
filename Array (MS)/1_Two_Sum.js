/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  var hashmap = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (hashmap.has(target - nums[i])) {
      return [hashmap.get(target - nums[i]), i];
    }

    hashmap.set(nums[i], i);
  }
};

// Niceee solution
