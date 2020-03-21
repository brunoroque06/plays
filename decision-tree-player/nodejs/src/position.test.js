const position = require('./position');

test('White to play in initial position', () => {
  const pos = position.createInitialPosition();
  expect(pos.result).toBe(position.Result.WHITE_TO_MOVE);
});

// test('Clone creates a new position', () => {
//   const pos = position.createInitialPosition();
//   const cloned = position.placePiece(pos, 0, 1);

//   expect(pos.board[0]).toBe(0);
//   expect(cloned.board[0]).toBe(1);
// });
