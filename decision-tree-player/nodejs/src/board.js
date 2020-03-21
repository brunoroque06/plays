const piece = {
  EMPTY: 0,
  WHITE: 1,
  BLACK: 2,
};

const getInitialBoard = () => [...Array(9)].map(() => piece.EMPTY);

module.exports = {
  getInitialBoard,
  Piece: piece,
};
