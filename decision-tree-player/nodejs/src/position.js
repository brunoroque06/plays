const board = require('./board');

const Result = {
  WHITE_TO_MOVE: 0,
  BLACK_TO_MOVE: 1,
  DRAW: 2,
  WHITE_WINS: 3,
  BLACK_WINS: 4,
};

function createInitialPosition() {
  return {
    board: board.getInitialBoard(),
    result: Result.WHITE_TO_MOVE,
  };
}

function assessPosition(position, result) {
  const
}

function playMove(pos, move) {
  // const newPos = board.placePiece(pos.board, move);
  // const result = getResult(pos.result, newPos);
  return 1;
}

module.exports = {
  createInitialPosition,
  playMove,
  Result,
};
