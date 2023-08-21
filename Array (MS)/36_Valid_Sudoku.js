/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  return isValidCol(board) && isValidRow(board);
};

// Check columns
var isValidCol = function (board) {
  const numCol = board[0].length;

  for (let i = 0; i < numCol; i++) {
    var hashmap = new Map();
    for (let j = 0; j < board.length; j++) {
      if (board[j][i] === ".") {
        continue;
      }
      if (hashmap.has(board[j][i])) {
        return false;
      }
      hashmap.set(board[j][i], true);
    }
  }

  return true;
};

// Check rows
var isValidRow = function (board) {
  const numCol = board[0].length;
  const numRow = board.length;

  for (let row = 0; row < numRow; row++) {
    var hashmap = new Map();
    for (let col = 0; col < numCol; col++) {
      if (board[row][col] === ".") {
        continue;
      }
      if (hashmap.has(board[row][col])) {
        return false;
      }
      hashmap.set(board[row][col], true);
    }
  }

  return true;
};

var isValidBox = function (board) {
  const numCol = board[0].length;
  const numRow = board.length;
  var boxCount = 1;

  for (let row = 0; row < numRow; row++) {
    var hashmap = new Map();
    for (let col = 0; col < numCol; col++) {
      if (board[row][col] === ".") {
        continue;
      }
      if (hashmap.has(board[row][col])) {
        return false;
      }
      hashmap.set(board[row][col], true);
    }
  }

  return true;
};

const board = [
  ["8", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

console.log(isValidSudoku(board));
