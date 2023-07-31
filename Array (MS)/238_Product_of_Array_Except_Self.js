/*
Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  var result = [];
  var leftMult = 1;
  var rightMult = 1;

  for (var i = nums.length - 1; i >= 0; i--) {
    result[i] = rightMult;
    rightMult *= nums[i];
  }

  for (var i = 0; i < nums.length; i++) {
    result[i] *= leftMult;
    leftMult *= nums[i];
  }

  return result;
};

productExceptSelf([1, 2, 3, 4]);

// Runtime - 100ms      | Beats 80.14% of users with JavaScript
// Memory - 51.76mb     | Beats 97.66% of users with JavaScript
