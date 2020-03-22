const Piece = {
  EMPTY: 0,
  WHITE: 1,
  BLACK: 2,
};

function createBoard(board) {
  return [...Array(9).keys()].map((i) => {
    if (board[i] === 'X') return Piece.WHITE;
    if (board[i] === 'O') return Piece.BLACK;
    return Piece.EMPTY;
  });
}

const createInitialBoard = () => createBoard(' '.repeat(9));

function placePiece(board, { square, piece }) {
  return [...Array(9).keys()].map((i) => {
    if (square === i) return piece;
    return board[i];
  });
}

module.exports = {
  createBoard,
  createInitialBoard,
  Piece,
  placePiece,
};
