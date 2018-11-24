package com.github.brunoroque06.games.board;

public enum Piece {
  X,
  O,
  Default;

  boolean isDefault() {
    return this == Piece.Default;
  }
}
