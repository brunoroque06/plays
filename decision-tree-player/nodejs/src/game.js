const position = require('./position');

function makeMove(pos) {
  return undefined;
}

function resolveGame(pos) {
  if (pos.result === position.Result.WHITE_TO_MOVE) {
    return resolveGame(makeMove(pos));
  }
  return pos;
}

function playGame() {
  const initialPos = position.createInitialPosition();
  return resolveGame(initialPos);
}

module.exports = {
  playGame,
};
