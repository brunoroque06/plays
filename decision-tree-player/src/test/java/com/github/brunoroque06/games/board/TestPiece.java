package com.github.brunoroque06.games.board;

public enum TestPiece implements Piece {
  WHITE,
  BLACK,
  EMPTY;

  @Override
  public boolean isWhite() {
    return this == WHITE;
  }
}
