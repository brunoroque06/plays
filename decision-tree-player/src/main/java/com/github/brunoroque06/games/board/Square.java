package com.github.brunoroque06.games.board;

class Square<T> {

  private final Coordinate coordinate;
  private final PieceFactory<T> pieceFactory;
  private T piece;

  Square(final Coordinate coordinate, final PieceFactory<T> pieceFactory) {
    this.coordinate = coordinate;
    this.pieceFactory = pieceFactory;
  }

  private Square(final Coordinate coordinate, final PieceFactory<T> pieceFactory, final T piece) {
    this.coordinate = coordinate;
    this.pieceFactory = pieceFactory;
    this.piece = piece;
  }

  void putWhite() {
    piece = pieceFactory.getWhite();
  }

  void putBlack() {
    piece = pieceFactory.getBlack();
  }

  void clear() {
    piece = pieceFactory.getEmpty();
  }

  boolean isEmpty() {
    return piece == pieceFactory.getEmpty();
  }

  Coordinate getCoordinate() {
    return coordinate;
  }

  Square<T> shallowClone() {
    return new Square<>(coordinate, pieceFactory, piece);
  }

  T getPiece() {
    return piece;
  }
}
