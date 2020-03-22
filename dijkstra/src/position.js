const board = require('./board');

const State = {
  WHITE_TO_MOVE: 0,
  BLACK_TO_MOVE: 1,
  DRAW: 2,
  WHITE_WINS: 3,
  BLACK_WINS: 4,
};

function createInitialPosition() {
  return {
    board: board.createInitialBoard(),
    state: State.WHITE_TO_MOVE,
  };
}

function evaluatePosition(brd, result) {
  if (brd[0] === brd[1] && brd[0] === brd[2] && brd[0] === board.Piece.WHITE) {
    return State.WHITE_WINS;
  }
  return State.BLACK_TO_MOVE;
}

function playMove(pos, move) {
  const brd = board.placePiece(pos.board, move);
  return { board: brd, state: evaluatePosition(brd, pos.state) };
}

module.exports = {
  createInitialPosition,
  playMove,
  State,
};
