const board = require('./board');

test('Initial board has 9 empty squares', () => {
  const initialBoard = board.getInitialBoard();

  expect(initialBoard.length).toBe(9);
  initialBoard.forEach((piece) => expect(piece).toBe(board.Piece.EMPTY));
});
