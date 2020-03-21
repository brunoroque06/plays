const Piece = {
  EMPTY: 0,
  WHITE: 1,
  BLACK: 2,
};

const getInitialBoard = () => [...Array(9)].map(() => Piece.EMPTY);

function placePiece(board, { square, piece }) {
  return [...Array(9).keys()].map((i) => {
    if (square === i) return piece;
    return board[i];
  });
}

module.exports = {
  getInitialBoard,
  Piece,
  placePiece,
};
