const board = require('./board');

test('Create board', () => {
  const brd = board.createBoard('XX O XOOX');
  expect(brd.length).toBe(9);
  expect(brd[0]).toBe(board.Piece.WHITE);
  expect(brd[1]).toBe(board.Piece.WHITE);
  expect(brd[2]).toBe(board.Piece.EMPTY);
  expect(brd[3]).toBe(board.Piece.BLACK);
  expect(brd[4]).toBe(board.Piece.EMPTY);
  expect(brd[5]).toBe(board.Piece.WHITE);
  expect(brd[6]).toBe(board.Piece.BLACK);
  expect(brd[7]).toBe(board.Piece.BLACK);
  expect(brd[8]).toBe(board.Piece.WHITE);
});

test('Initial board has 9 empty squares', () => {
  const brd = board.createInitialBoard();
  expect(brd.length).toBe(9);
  brd.forEach((piece) => expect(piece).toBe(board.Piece.EMPTY));
});

test('Place piece clones the board', () => {
  const brd = [...Array(9).keys()].map(() => board.Piece.EMPTY);
  const clonedBrd = board.placePiece(brd, {
    square: 0,
    piece: board.Piece.WHITE,
  });
  expect(brd[0]).toBe(board.Piece.EMPTY);
  expect(clonedBrd.length).toBe(9);
  expect(clonedBrd[0]).toBe(board.Piece.WHITE);
});
