/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // Create an object
  let map = {};
  // The array of the primes for mapping
  let primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101,
  ];

  strs.forEach((str) => {
    let key = str
      .split("") // Make a string to an array
      .reduce((r, c) => r * primes[c.charCodeAt() - 97], 1);
    // Since we are gonna multiply the primes by each code of the character,
    // the key value would be unique.
    // Therefore, if the words are anagram, they should have the same key value.
    map[key] ? map[key].push(str) : (map[key] = [str]);
  });

  return Object.values(map);
};

// Reference: Leetcode @liushuaimaya
