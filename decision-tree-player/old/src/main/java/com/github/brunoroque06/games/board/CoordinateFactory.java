package com.github.brunoroque06.games.board;

public class CoordinateFactory {

  public Coordinate create(final int row, final int col) {
    return new Coordinate(row, col);
  }
}
