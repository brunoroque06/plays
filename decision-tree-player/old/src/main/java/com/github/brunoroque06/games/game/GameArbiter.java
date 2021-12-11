package com.github.brunoroque06.games.game;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Piece;
import com.github.brunoroque06.games.players.Player;

public class GameArbiter<T extends Piece> {
  private final Board<T> board;
  private final Player<T> whitePlayer;
  private final Player<T> blackPlayer;
  private final Game<T> game;

  public GameArbiter(
      final Board<T> board,
      final Player<T> whitePlayer,
      final Player<T> blackPlayer,
      final Game<T> game) {
    this.board = board;
    this.whitePlayer = whitePlayer;
    this.blackPlayer = blackPlayer;
    this.game = game;
  }

  GameResult play() {
    while (!game.isOver(board)) {
      makeWhiteMove();
      if (game.isOver(board)) {
        return game.getResult(board);
      }
      makeBlackMove();
    }
    return game.getResult(board);
  }

  private void makeWhiteMove() {
    final var whiteMove = whitePlayer.chooseMove(board);
    board.playMove(whiteMove);
  }

  private void makeBlackMove() {
    final var blackMove = blackPlayer.chooseMove(board);
    board.playMove(blackMove);
  }

  void resetGame() {
    board.resetBoard();
  }
}
