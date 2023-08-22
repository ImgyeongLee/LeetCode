/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    let middleIdx = Math.round(start + end / 2);
    if (nums[middleIdx] === target) return middleIdx;
    else if (nums[middleIdx] > target) end -= 1;
    else start += 1;
  }

  return -1;
};

const nums = [-1, 0, 3, 5, 8, 12];
const target = 9;

console.log(search(nums, target));

// Runtime - 55ms       | Beats 79.06% of users with JavaScript
// Memory - 45.57mb     | Beats 7.43% of users with JavaScript
