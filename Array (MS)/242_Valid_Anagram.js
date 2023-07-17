/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length != t.length) {
    return false;
  }

  var map1 = new Map();
  var map2 = new Map();
  var letters = new Set(t);

  for (let i = 0; i < s.length; i++) {
    if (map1.has(s[i])) {
      map1.set(s[i], map1.get(s[i]) + 1);
    } else {
      map1.set(s[i], 1);
    }

    if (map2.has(t[i])) {
      map2.set(t[i], map2.get(t[i]) + 1);
    } else {
      map2.set(t[i], 1);
    }
  }

  for (let letter of letters) {
    if (map1.get(letter) != map2.get(letter)) {
      return false;
    }
  }

  return true;
};

console.log(isAnagram("cat", "rac"));
