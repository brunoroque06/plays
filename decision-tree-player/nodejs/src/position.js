const board = require('./board');

const result = {
  WHITE_TO_MOVE: 0,
  BLACK_TO_MOVE: 1,
  DRAW: 2,
  WHITE_WINS: 3,
  BLACK_WINS: 4,
};

function createInitialPosition() {
  return {
    board: board.getInitialBoard(),
    result: result.WHITE_TO_MOVE,
  };
}

module.exports = { createInitialPosition, Result: result };
