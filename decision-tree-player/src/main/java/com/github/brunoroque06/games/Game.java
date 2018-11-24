package com.github.brunoroque06.games;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.players.Player;

class Game {
  private final Board board;
  private final Player playerX;
  private final Player playerO;

  Game(final Board board, final Player playerX, final Player playerO) {
    this.board = board;
    this.playerX = playerX;
    this.playerO = playerO;
  }

  Board getBoard() {
    return board;
  }

  Board process() {
    while (!board.getStatus().isGameWonOrDrawn()) {
      final var playerToPlay = isPlayerXToPlay() ? playerX : playerO;
      makePlayerPlayMove(playerToPlay);
    }
    return board.cloneBoard();
  }

  private boolean isPlayerXToPlay() {
    return board.getStatus().isXTurn();
  }

  private void makePlayerPlayMove(final Player player) {
    final var move = player.chooseMove(board);
    board.playPieceAndUpdateState(move);
  }

  void resetGame() {
    board.resetBoard();
  }
}
