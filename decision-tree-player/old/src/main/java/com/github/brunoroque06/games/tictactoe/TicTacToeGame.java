package com.github.brunoroque06.games.tictactoe;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.CoordinateFactory;
import com.github.brunoroque06.games.game.Game;
import com.github.brunoroque06.games.game.GameResult;
import java.util.ArrayList;

public class TicTacToeGame implements Game<TicTacToePiece> {

  private final CoordinateFactory coordinateFactory;

  public TicTacToeGame(final CoordinateFactory coordinateFactory) {
    this.coordinateFactory = coordinateFactory;
  }

  @Override
  public float evaluatePosition(final Board<TicTacToePiece> board) {
    return evaluate(board);
  }

  @Override
  public boolean isOver(final Board<TicTacToePiece> board) {
    final var evaluation = evaluate(board);
    return evaluation != 0 || board.isFull();
  }

  @Override
  public GameResult getResult(final Board<TicTacToePiece> board) {
    final var evaluation = evaluate(board);
    if (evaluation == Float.POSITIVE_INFINITY) {
      return GameResult.WHITE_WON;
    } else if (evaluation == Float.NEGATIVE_INFINITY) {
      return GameResult.BLACK_WON;
    } else {
      return GameResult.DRAW;
    }
  }

  private float evaluate(final Board<TicTacToePiece> board) {
    final var evaluations = new ArrayList<Float>(8);
    evaluations.add(evaluateLine(board, 0, 0, 0, 1, 0, 2));
    evaluations.add(evaluateLine(board, 1, 0, 1, 1, 1, 2));
    evaluations.add(evaluateLine(board, 2, 0, 2, 1, 2, 2));

    evaluations.add(evaluateLine(board, 0, 0, 1, 0, 2, 0));
    evaluations.add(evaluateLine(board, 0, 1, 1, 1, 2, 1));
    evaluations.add(evaluateLine(board, 0, 2, 1, 2, 2, 2));

    evaluations.add(evaluateLine(board, 0, 0, 1, 1, 2, 2));
    evaluations.add(evaluateLine(board, 2, 0, 1, 1, 0, 2));
    return evaluations.stream().filter(e -> e != 0).findFirst().orElse(0F);
  }

  private float evaluateLine(
      final Board<TicTacToePiece> board,
      final int row0,
      final int col0,
      final int row1,
      final int col1,
      final int row2,
      final int col2) {

    final var piece0 = board.getPiece(coordinateFactory.create(row0, col0));
    final var piece1 = board.getPiece(coordinateFactory.create(row1, col1));
    final var piece2 = board.getPiece(coordinateFactory.create(row2, col2));
    if (isLine(piece0, piece1, piece2)) {
      return getEvaluation(piece0);
    } else {
      return 0L;
    }
  }

  private boolean isLine(
      final TicTacToePiece piece0, final TicTacToePiece piece1, final TicTacToePiece piece2) {
    return piece0 == piece1 && piece0 == piece2 && piece0 != TicTacToePiece.EMPTY;
  }

  private float getEvaluation(final TicTacToePiece piece) {
    return piece == TicTacToePiece.WHITE ? Float.POSITIVE_INFINITY : Float.NEGATIVE_INFINITY;
  }
}
