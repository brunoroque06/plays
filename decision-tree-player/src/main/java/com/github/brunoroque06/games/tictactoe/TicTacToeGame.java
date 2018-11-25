package com.github.brunoroque06.games.tictactoe;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.CoordinateFactory;
import com.github.brunoroque06.games.game.Game;
import com.github.brunoroque06.games.game.GameResult;

public class TicTacToeGame implements Game<TicTacToePiece> {

  private final CoordinateFactory coordinateFactory;

  public TicTacToeGame(final CoordinateFactory coordinateFactory) {
    this.coordinateFactory = coordinateFactory;
  }

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
    return evaluate(board) == GameResult.WHITE_WON || evaluate(board) == GameResult.BLACK_WON;
  }

  private GameResult evaluate(final Board<TicTacToePiece> board) {
    final var firstLine =
        isLine(
            board,
            coordinateFactory.create(0, 0),
            coordinateFactory.create(0, 1),
            coordinateFactory.create(0, 2));
    if (firstLine) {
      return board.getPiece(coordinateFactory.create(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var secondLine =
        isLine(
            board,
            coordinateFactory.create(1, 0),
            coordinateFactory.create(1, 1),
            coordinateFactory.create(1, 2));
    if (secondLine) {
      return board.getPiece(coordinateFactory.create(1, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var thirdLine =
        isLine(
            board,
            coordinateFactory.create(2, 0),
            coordinateFactory.create(2, 1),
            coordinateFactory.create(2, 2));
    if (thirdLine) {
      return board.getPiece(coordinateFactory.create(2, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }

    final var firstCol =
        isLine(
            board,
            coordinateFactory.create(0, 0),
            coordinateFactory.create(1, 0),
            coordinateFactory.create(2, 0));
    if (firstCol) {
      return board.getPiece(coordinateFactory.create(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var secondCol =
        isLine(
            board,
            coordinateFactory.create(0, 1),
            coordinateFactory.create(1, 1),
            coordinateFactory.create(2, 1));
    if (secondCol) {
      return board.getPiece(coordinateFactory.create(0, 1)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var thirdCol =
        isLine(
            board,
            coordinateFactory.create(0, 2),
            coordinateFactory.create(1, 2),
            coordinateFactory.create(2, 2));
    if (thirdCol) {
      return board.getPiece(coordinateFactory.create(0, 2)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var negativeDiagonal =
        isLine(
            board,
            coordinateFactory.create(0, 0),
            coordinateFactory.create(1, 1),
            coordinateFactory.create(2, 2));
    if (negativeDiagonal) {
      return board.getPiece(coordinateFactory.create(0, 0)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    final var positiveDiagonal =
        isLine(
            board,
            coordinateFactory.create(0, 2),
            coordinateFactory.create(1, 1),
            coordinateFactory.create(2, 0));
    if (positiveDiagonal) {
      return board.getPiece(coordinateFactory.create(0, 2)) == TicTacToePiece.WHITE
          ? GameResult.WHITE_WON
          : GameResult.BLACK_WON;
    }
    return GameResult.DRAW;
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
