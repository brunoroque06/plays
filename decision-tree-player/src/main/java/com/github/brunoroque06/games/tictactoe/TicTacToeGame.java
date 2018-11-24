package com.github.brunoroque06.games.tictactoe;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.game.Game;
import com.github.brunoroque06.games.game.GameResult;

public class TicTacToeGame implements Game<TicTacToePiece> {

  @Override
  public float evaluatePosition(final Board<TicTacToePiece> board) {
    final var result = evaluate(board);
    if (result == GameResult.WHITE_WON) {
      return Float.POSITIVE_INFINITY;
    } else if (result == GameResult.BLACK_WON) {
      return Float.NEGATIVE_INFINITY;
    }
    return 0;
  }

  @Override
  public boolean isOver(final Board<TicTacToePiece> board) {
    return isGameWon(board) || board.isFull();
  }

  @Override
  public GameResult getResult(final Board<TicTacToePiece> board) {
    return evaluate(board);
  }

  private boolean isGameWon(final Board<TicTacToePiece> board) {
    if (evaluate(board) == null) {
      return false;
    } else {
      return true;
    }
  }

  private GameResult evaluate(final Board<TicTacToePiece> board) {
    final var firstLine =
        isLine(board, new Coordinate(0, 0), new Coordinate(0, 1), new Coordinate(0, 2));
    if (firstLine) {
      return board.getPiece(new Coordinate(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var secondLine =
        isLine(board, new Coordinate(1, 0), new Coordinate(1, 1), new Coordinate(1, 2));
    if (secondLine) {
      return board.getPiece(new Coordinate(1, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var thirdLine =
        isLine(board, new Coordinate(2, 0), new Coordinate(2, 1), new Coordinate(2, 2));
    if (thirdLine) {
      return board.getPiece(new Coordinate(2, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }

    final var firstCol =
        isLine(board, new Coordinate(0, 0), new Coordinate(1, 0), new Coordinate(2, 0));
    if (firstCol) {
      return board.getPiece(new Coordinate(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var secondCol =
        isLine(board, new Coordinate(0, 1), new Coordinate(1, 1), new Coordinate(2, 1));
    if (secondCol) {
      return board.getPiece(new Coordinate(0, 1)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var thirdCol =
        isLine(board, new Coordinate(0, 2), new Coordinate(1, 2), new Coordinate(2, 2));
    if (thirdCol) {
      return board.getPiece(new Coordinate(0, 2)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var negativeDiagonal =
        isLine(board, new Coordinate(0, 0), new Coordinate(1, 1), new Coordinate(2, 2));
    if (negativeDiagonal) {
      return board.getPiece(new Coordinate(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var positiveDiagonal =
        isLine(board, new Coordinate(0, 2), new Coordinate(1, 1), new Coordinate(2, 0));
    if (positiveDiagonal) {
      return board.getPiece(new Coordinate(0, 2)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    return null;
  }

  private boolean isLine(
      final Board<TicTacToePiece> board,
      final Coordinate first,
      final Coordinate second,
      final Coordinate third) {
    final var firstPiece = board.getPiece(first);
    final var secondPiece = board.getPiece(second);
    final var thirdPiece = board.getPiece(third);
    return firstPiece == secondPiece
        && firstPiece == thirdPiece
        && firstPiece != TicTacToePiece.EMPTY;
  }
}
