const board = require('./board');
const position = require('./position');

test('White to play in initial position', () => {
  const pos = position.createInitialPosition();
  expect(pos.state).toBe(position.State.WHITE_TO_MOVE);
});

// test('Clone creates a new position', () => {
//   const pos = position.createInitialPosition();
//   const cloned = position.placePiece(pos, 0, 1);

//   expect(pos.board[0]).toBe(0);
//   expect(cloned.board[0]).toBe(1);
// });

test('Top row white wins', () => {
  const brd = board.createBoard(' XX      ');
  const newPos = position.playMove(
    { board: brd, state: position.State.WHITE_TO_MOVE },
    {
      square: 0,
      piece: board.Piece.WHITE,
    },
  );

  expect(brd[0]).toBe(board.Piece.EMPTY);
  expect(newPos.board[0]).toBe(board.Piece.WHITE);
  expect(newPos.result).toBe(position.State.WHITE_WINS);
});
