const board = require('./board');

test('Initial board has 9 empty squares', () => {
  const initialBoard = board.getInitialBoard();

  expect(initialBoard.length).toBe(9);
  initialBoard.forEach((piece) => expect(piece).toBe(board.Piece.EMPTY));
});

test('Place piece clones the board', () => {
  const newBoard = [...Array(9).keys()].map(() => board.Piece.EMPTY);
  const clonedBoard = board.placePiece(newBoard, {
    square: 0,
    piece: board.Piece.WHITE,
  });

  expect(newBoard[0]).toBe(board.Piece.EMPTY);
  expect(clonedBoard.length).toBe(9);
  expect(clonedBoard[0]).toBe(board.Piece.WHITE);
});
