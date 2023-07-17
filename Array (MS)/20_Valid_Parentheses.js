/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  var opening = ["(", "{", "["];
  var closing = [")", "}", "]"];
  var stack = [];
  for (letter of s) {
    if (opening.includes(letter)) {
      stack.push(letter);
    } else if (closing.includes(letter)) {
      let el = stack.pop();

      if (
        !(
          (letter === ")" && el === "(") ||
          (letter === "}" && el === "{") ||
          (letter === "]" && el === "[")
        )
      ) {
        return false;
      }
    }
  }

  if (stack.length) {
    return false;
  }

  return true;
};
