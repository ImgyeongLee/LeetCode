/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const newString = s.replace(/[^\w\s]|_/g, "").replace(/\s+/g, "");
  var leftPointer = 0;
  var rightPointer = 0;
  for (let i = 0; i < newString.length / 2; i++) {
    if (
      newString[i].toLowerCase() ===
      newString[newString.length - 1 - i].toLowerCase()
    ) {
      rightPointer += 1;
    }
    leftPointer += 1;
  }

  return rightPointer === leftPointer ? true : false;
};

console.log(isPalindrome("race a car"));
