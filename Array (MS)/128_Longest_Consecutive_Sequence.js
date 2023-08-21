/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length == 0) {
    return 0;
  }

  nums.sort(function (a, b) {
    return a - b;
  });

  console.log("Sorted version == ", nums);

  var count = 1;
  var result = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] === nums[i]) {
      continue;
    }
    nums[i - 1] - nums[i] === -1 ? (count += 1) : (count = 1);
    if (count > result) {
      result = count;
    }
  }

  return result;
};

// Runtime - 101ms      | Beats 83.11% of users with JavaScript
// Memory - 51.36mb     | Beats 97.84% of users with JavaScript
