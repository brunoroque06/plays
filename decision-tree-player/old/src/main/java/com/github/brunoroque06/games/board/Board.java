package com.github.brunoroque06.games.board;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Board<T extends Piece> {
  private final int rows;
  private final int cols;
  private final List<Square<T>> board;
  private final PieceFactory<T> pieceFactory;
  private T toMove;

  public Board(final int rows, final int cols, final PieceFactory<T> pieceFactory) {
    this.rows = rows;
    this.cols = cols;
    this.pieceFactory = pieceFactory;
    board = new ArrayList<>(rows * cols);
    createSquares();
    resetBoard();
  }

  public void resetBoard() {
    board.forEach(Square::clear);
    toMove = pieceFactory.getWhite();
  }

  private void createSquares() {
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        final var square = new Square<>(new Coordinate(r, c), pieceFactory);
        square.clear();
        final var index = estimateIndex(new Coordinate(r, c));
        board.add(index, square);
      }
    }
  }

  private int estimateIndex(final Coordinate coordinate) {
    return coordinate.getCol() + coordinate.getRow() * cols;
  }

  private Board(
      final int rows,
      final int cols,
      final List<Square<T>> board,
      final PieceFactory<T> pieceFactory,
      final T toMove) {
    this.cols = cols;
    this.rows = rows;
    this.pieceFactory = pieceFactory;
    this.board = board;
    this.toMove = toMove;
  }

  public boolean isFull() {
    return board.stream().noneMatch(Square::isEmpty);
  }

  public boolean isEmpty() {
    return board.stream().allMatch(Square::isEmpty);
  }

  public List<Coordinate> getEmptyCoordinates() {
    return board
        .stream()
        .filter(Square::isEmpty)
        .map(Square::getCoordinate)
        .collect(Collectors.toList());
  }

  public T getToMove() {
    return toMove;
  }

  public Board<T> shallowClone() {
    final var clone = new ArrayList<Square<T>>(board.size());
    for (final var square : board) clone.add(square.shallowClone());
    return new Board<>(rows, cols, clone, pieceFactory, toMove);
  }

  public void playMove(final Coordinate coordinate) {
    final var index = estimateIndex(coordinate);
    if (toMove == pieceFactory.getWhite()) {
      board.get(index).putWhite();
      toMove = pieceFactory.getBlack();
    } else {
      board.get(index).putBlack();
      toMove = pieceFactory.getWhite();
    }
  }

  public T getPiece(final Coordinate coordinate) {
    final var index = estimateIndex(coordinate);
    return board.get(index).getPiece();
  }
}
