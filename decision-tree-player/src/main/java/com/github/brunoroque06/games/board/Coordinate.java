package com.github.brunoroque06.games.board;

public class Coordinate {

  private final int row;
  private final int col;

  public Coordinate(final int row, final int col) {
    this.row = row;
    this.col = col;
  }

  public int getRow() {
    return row;
  }

  public int getCol() {
    return col;
  }
}
